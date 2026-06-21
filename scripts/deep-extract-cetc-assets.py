#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CETC_ROOT = Path("/Users/cuizihao/CETC/Project")
OUTPUTS_DIR = ROOT / "outputs"
JSON_PATH = OUTPUTS_DIR / "cetc-deep-asset-extraction.json"
MD_PATH = OUTPUTS_DIR / "cetc-deep-asset-extraction.md"
REFERENCE_PATH = ROOT / "30_References" / "cetc-high-value-project-deep-assets.md"

EXCLUDED_DIRS = {
    ".git",
    ".idea",
    ".vscode",
    "node_modules",
    "dist",
    "build",
    "target",
    "coverage",
    "logs",
    "tmp",
    "temp",
    ".cache",
    ".nuxt",
    ".next",
    "arcgis_js_api",
}

HIGH_VALUE_PROJECTS = [
    "jun-dd-web",
    "cetc-ui/bi-ui",
    "gis/gis-map-sdk",
    "gis/gis-map-sdk-cesium",
    "gis/gis-map-develop-platform",
    "cgpt2.0/city-manage-h5",
    "cgpt2.0/city-manage-server",
    "cgpt2.0/e-city-big",
    "xinfang/xinfang",
    "xinfang/xinfang-web-admin",
]

CODE_SUFFIXES = {
    ".vue",
    ".js",
    ".ts",
    ".jsx",
    ".tsx",
    ".java",
    ".xml",
    ".yml",
    ".yaml",
    ".properties",
    ".json",
    ".md",
    ".scss",
    ".less",
    ".css",
}

SENSITIVE_RE = re.compile(
    r"password|passwd|pwd|secret|token|access[_-]?key|client_secret|Bearer|账号|密码|ak|sk",
    re.I,
)
ROUTE_RE = re.compile(r"\bpath\s*:\s*['\"]([^'\"]+)['\"]")
API_RE = re.compile(r"\b(?:url\s*:\s*|request\(|axios\.[a-z]+\(|fetch\() ['\"]([^'\"]+)['\"]", re.X)
JAVA_MAPPING_RE = re.compile(r"@(?:RequestMapping|GetMapping|PostMapping|PutMapping|DeleteMapping)\s*\(([^)]*)\)")


def rel(path: Path, base: Path) -> str:
    return path.relative_to(base).as_posix()


def iter_files(project: Path):
    for root, dirs, files in os.walk(project):
        dirs[:] = [item for item in dirs if item not in EXCLUDED_DIRS and not item.startswith(".")]
        root_path = Path(root)
        for file_name in files:
            path = root_path / file_name
            if path.suffix.lower() in CODE_SUFFIXES:
                yield path


def read_text(path: Path, max_chars: int = 120_000) -> str:
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return ""
    return text[:max_chars]


def collect_by_suffix(project: Path, suffixes: set[str], limit: int = 120) -> list[str]:
    items = [rel(path, project) for path in iter_files(project) if path.suffix.lower() in suffixes]
    return sorted(set(items))[:limit]


def collect_named_dirs(project: Path, names: set[str], limit: int = 80) -> list[str]:
    items = []
    for root, dirs, _files in os.walk(project):
        dirs[:] = [item for item in dirs if item not in EXCLUDED_DIRS and not item.startswith(".")]
        root_path = Path(root)
        for item in dirs:
            if item in names:
                items.append(rel(root_path / item, project))
    return sorted(set(items))[:limit]


def collect_routes(project: Path, limit: int = 120) -> list[dict[str, str]]:
    routes = []
    for path in iter_files(project):
        path_text = path.as_posix().lower()
        if "router" not in path_text and path.name not in {"routes.js", "routes.ts", "permission.js"}:
            continue
        text = read_text(path)
        for match in ROUTE_RE.finditer(text):
            routes.append({"file": rel(path, project), "path": match.group(1)})
    return routes[:limit]


def collect_api_endpoints(project: Path, limit: int = 160) -> list[dict[str, str]]:
    endpoints = []
    for path in iter_files(project):
        lower = path.as_posix().lower()
        if path.suffix.lower() == ".java":
            text = read_text(path)
            for match in JAVA_MAPPING_RE.finditer(text):
                value = match.group(1).replace("\n", " ").strip()
                endpoints.append({"file": rel(path, project), "endpoint": value[:140]})
            continue
        if "/api/" not in lower and "request" not in lower and "service" not in lower:
            continue
        text = read_text(path)
        for match in API_RE.finditer(text):
            endpoints.append({"file": rel(path, project), "endpoint": match.group(1)})
    deduped = []
    seen = set()
    for item in endpoints:
        key = (item["file"], item["endpoint"])
        if key not in seen:
            deduped.append(item)
            seen.add(key)
    return deduped[:limit]


def collect_components(project: Path, limit: int = 120) -> list[str]:
    component_dirs = {"/components/", "/component/", "/packages/", "/src/lib/", "/src/libs/"}
    items = []
    for path in iter_files(project):
        text_path = f"/{rel(path, project)}"
        if path.suffix.lower() in {".vue", ".js", ".ts"} and any(marker in text_path for marker in component_dirs):
            items.append(rel(path, project))
    return sorted(set(items))[:limit]


def collect_gis_assets(project: Path, limit: int = 120) -> list[str]:
    gis_terms = (
        "map",
        "gis",
        "arcgis",
        "cesium",
        "leaflet",
        "openlayers",
        "amap",
        "geojson",
        "shp",
        "tiles",
        "layer",
    )
    items = []
    for path in iter_files(project):
        rp = rel(path, project)
        lower = rp.lower()
        if any(term in lower for term in gis_terms):
            items.append(rp)
            continue
        text = read_text(path, 20_000).lower()
        if any(term in text for term in gis_terms[:8]):
            items.append(rp)
    return sorted(set(items))[:limit]


def collect_config_and_risks(project: Path, limit: int = 120) -> tuple[list[str], list[str]]:
    config_files = []
    sensitive_files = []
    for path in iter_files(project):
        rp = rel(path, project)
        name = path.name.lower()
        if name.startswith(".env") or "config" in name or path.suffix.lower() in {".yml", ".yaml", ".properties"}:
            config_files.append(rp)
        text = read_text(path, 30_000)
        if SENSITIVE_RE.search(text):
            sensitive_files.append(rp)
    return sorted(set(config_files))[:limit], sorted(set(sensitive_files))[:limit]


def detect_stack(project: Path) -> dict[str, object]:
    stack: dict[str, object] = {"kind": "unknown", "scripts": [], "dependencies": []}
    package_path = project / "package.json"
    pom_path = project / "pom.xml"
    if package_path.exists():
        try:
            data = json.loads(package_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            data = {}
        deps = sorted({*(data.get("dependencies") or {}).keys(), *(data.get("devDependencies") or {}).keys()})
        stack = {
            "kind": "frontend",
            "name": data.get("name", ""),
            "scripts": sorted((data.get("scripts") or {}).keys()),
            "dependencies": deps[:40],
        }
    if pom_path.exists():
        text = read_text(pom_path)
        artifact = re.search(r"<artifactId>\s*([^<]+)\s*</artifactId>", text)
        stack = {
            "kind": "java",
            "artifactId": artifact.group(1) if artifact else "",
            "dependencies": re.findall(r"<artifactId>\s*([^<]+)\s*</artifactId>", text)[:40],
        }
    return stack


def infer_asset_value(project_id: str, summary: dict[str, object]) -> str:
    if project_id in {"jun-dd-web", "cetc-ui/bi-ui"}:
        return "BI 大屏、可视化组件、GIS 页面和前端工程经验，可作为组件/页面/样式资产继续复用。"
    if project_id == "gis/gis-map-sdk":
        return "WebGIS SDK 抽象价值高，适合作为地图图层、工具函数和二次开发样板。"
    if project_id == "gis/gis-map-sdk-cesium":
        return "3D GIS/Cesium 能力沉淀价值高，适合保留相机、图层、实体、场景初始化模式。"
    if project_id == "gis/gis-map-develop-platform":
        return "地图开发平台样板价值高，但配置风险也较高，适合脱敏后保留。"
    if project_id.startswith("cgpt2.0/"):
        return "城市治理链路资产，适合抽业务流程、移动端页面、大屏指标和后端接口。"
    if project_id.startswith("xinfang/"):
        return "信访业务链路资产，适合抽业务对象、权限结构、工单流转和后台页面。"
    return "具备专题资产价值，建议保留到抽取完成后再决定归档。"


def summarize_project(project_id: str) -> dict[str, object]:
    project = CETC_ROOT / project_id
    if not project.exists():
        return {"project": project_id, "exists": False}
    routes = collect_routes(project)
    endpoints = collect_api_endpoints(project)
    pages = collect_by_suffix(project, {".vue", ".tsx", ".jsx"}, 160)
    components = collect_components(project)
    gis_assets = collect_gis_assets(project)
    config_files, sensitive_files = collect_config_and_risks(project)
    dirs = collect_named_dirs(project, {"views", "pages", "components", "api", "router", "store", "service", "controller", "mapper", "modules", "packages"})
    stack = detect_stack(project)
    summary = {
        "project": project_id,
        "path": str(project),
        "exists": True,
        "stack": stack,
        "assetValue": "",
        "dirs": dirs,
        "routes": routes,
        "pages": pages,
        "components": components,
        "apiEndpoints": endpoints,
        "gisAssets": gis_assets,
        "configFiles": config_files,
        "sensitiveSignalFiles": sensitive_files,
        "counts": {
            "dirs": len(dirs),
            "routes": len(routes),
            "pages": len(pages),
            "components": len(components),
            "apiEndpoints": len(endpoints),
            "gisAssets": len(gis_assets),
            "configFiles": len(config_files),
            "sensitiveSignalFiles": len(sensitive_files),
        },
    }
    summary["assetValue"] = infer_asset_value(project_id, summary)
    return summary


def bullet(items: list[str], limit: int = 14, empty: str = "未发现") -> list[str]:
    if not items:
        return [f"- {empty}"]
    lines = [f"- `{item}`" for item in items[:limit]]
    if len(items) > limit:
        lines.append(f"- ... 另有 {len(items) - limit} 项")
    return lines


def render_pair_items(items: list[dict[str, str]], key: str, limit: int = 16, empty: str = "未发现") -> list[str]:
    if not items:
        return [f"- {empty}"]
    lines = [f"- `{item.get(key, '')}` in `{item.get('file', '')}`" for item in items[:limit]]
    if len(items) > limit:
        lines.append(f"- ... 另有 {len(items) - limit} 项")
    return lines


def render_markdown(report: dict[str, object]) -> str:
    projects = report["projects"]
    existing = [item for item in projects if item.get("exists")]
    stack_counts = Counter(item["stack"].get("kind", "unknown") for item in existing)
    lines = [
        "---",
        "title: CETC 高价值项目深度资产报告",
        "tags: [reference, code, cetc, deep-extraction, generated]",
        f"created: {report['date']}",
        "source: /Users/cuizihao/CETC/Project",
        "related: [CETC 自动资产抽取报告, CETC 旧项目业务价值与架构判断]",
        "---",
        "",
        "# CETC 高价值项目深度资产报告",
        "",
        f"> 生成时间：{report['generatedAt']}",
        "",
        "## 总览",
        "",
        f"- 目标项目：{len(projects)} 个",
        f"- 实际存在：{len(existing)} 个",
        f"- JSON 输出：`outputs/cetc-deep-asset-extraction.json`",
        f"- Markdown 输出：`outputs/cetc-deep-asset-extraction.md`",
        "",
        "| 类型 | 数量 |",
        "| --- | ---: |",
    ]
    for key, count in sorted(stack_counts.items()):
        lines.append(f"| `{key}` | {count} |")
    lines.extend(
        [
            "",
            "## 资产矩阵",
            "",
            "| 项目 | 类型 | 页面 | 路由 | 组件 | API/接口 | GIS 线索 | 风险线索 |",
            "| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for item in existing:
        counts = item["counts"]
        lines.append(
            f"| `{item['project']}` | `{item['stack'].get('kind', 'unknown')}` | "
            f"{counts['pages']} | {counts['routes']} | {counts['components']} | "
            f"{counts['apiEndpoints']} | {counts['gisAssets']} | {counts['sensitiveSignalFiles']} |"
        )
    lines.extend(["", "## 项目深挖", ""])
    for item in projects:
        lines.extend([f"### {item['project']}", ""])
        if not item.get("exists"):
            lines.extend(["- 状态：项目目录不存在，可能已归档或移动。", ""])
            continue
        stack = item["stack"]
        lines.extend(
            [
                f"- 类型：`{stack.get('kind', 'unknown')}`",
                f"- 资产价值：{item['assetValue']}",
                f"- 依赖样本：`{', '.join(stack.get('dependencies', [])[:12]) or '未发现'}`",
                f"- 脚本/构建入口：`{', '.join(stack.get('scripts', [])) or '未发现'}`",
                "",
                "关键目录：",
                *bullet(item["dirs"], 10),
                "",
                "路由入口：",
                *render_pair_items(item["routes"], "path", 14),
                "",
                "页面样本：",
                *bullet(item["pages"], 16),
                "",
                "组件/库样本：",
                *bullet(item["components"], 16),
                "",
                "API/后端接口样本：",
                *render_pair_items(item["apiEndpoints"], "endpoint", 16),
                "",
                "GIS/地图/可视化线索：",
                *bullet(item["gisAssets"], 16),
                "",
                "配置文件线索：",
                *bullet(item["configFiles"], 14),
                "",
                "敏感关键词线索：",
                *bullet(item["sensitiveSignalFiles"], 14),
                "",
            ]
        )
    lines.extend(
        [
            "## 下一步动作",
            "",
            "- `jun-dd-web` 和 `cetc-ui/bi-ui`：优先抽取通用可视化组件、地图页面、图表封装。",
            "- `gis-map-sdk` 和 `gis-map-sdk-cesium`：沉淀 SDK 能力边界、初始化流程、图层/实体/工具函数清单。",
            "- `cgpt2.0` 链路：按移动端、后端、大屏拆成城市治理业务知识。",
            "- `xinfang` 链路：按业务对象、流程状态、后台权限和页面结构拆成信访业务知识。",
            "- 带敏感关键词线索的项目：只记录风险文件路径和风险类型，不把配置原文进入公开知识库。",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    generated_at = datetime.now(timezone.utc).isoformat()
    report = {
        "generatedAt": generated_at,
        "date": datetime.now().date().isoformat(),
        "source": str(CETC_ROOT),
        "projects": [summarize_project(project_id) for project_id in HIGH_VALUE_PROJECTS],
    }
    OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)
    JSON_PATH.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    markdown = render_markdown(report)
    MD_PATH.write_text(markdown, encoding="utf-8")
    REFERENCE_PATH.write_text(markdown, encoding="utf-8")
    existing_count = sum(1 for item in report["projects"] if item.get("exists"))
    print(f"Generated deep asset report for {existing_count}/{len(HIGH_VALUE_PROJECTS)} projects.")
    print(f"Wrote {JSON_PATH.relative_to(ROOT)}")
    print(f"Wrote {REFERENCE_PATH.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
