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
REFERENCE_PATH = ROOT / "30_References" / "cetc-asset-extraction-report.md"
JSON_PATH = OUTPUTS_DIR / "cetc-asset-extraction.json"
MD_PATH = OUTPUTS_DIR / "cetc-asset-extraction.md"

EXCLUDED_DIRS = {
    ".git",
    "node_modules",
    "dist",
    "build",
    "target",
    ".idea",
    ".vscode",
    "coverage",
    "static",
    "arcgis_js_api",
    "library",
    "assets",
}

ACTION_RULES = {
    "cetc-ui/compass-ui-demo": "摘要后可删",
    "smartCity/managerweb": "摘要后可删",
    "industry-chain": "摘要后可删",
    "gis/offline-map": "摘要后可删",
    "cgpt2.0/city-mange-ui-web": "先脱敏后归档",
    "xinfang/xinfang-web": "先脱敏后归档",
    "BeijingDaxing/cetc-moniwa-ui": "先脱敏后归档",
    "gis/gis-map-develop-platform": "先脱敏后保留",
    "jun-dd-web": "保留",
    "cetc-ui/bi-ui": "保留",
    "gis/gis-map-sdk": "保留",
    "gis/gis-map-sdk-cesium": "保留",
}

HIGH_VALUE_PREFIXES = ("cgpt2.0/", "xinfang/")
HIGH_VALUE_NAMES = {
    "jun-dd-web",
    "cetc-ui/bi-ui",
    "gis/gis-map-sdk",
    "gis/gis-map-sdk-cesium",
    "gis/gis-map-develop-platform",
}

CONFIG_NAMES = {
    "vue.config.js",
    "application.yml",
    "application.properties",
    "app.properties",
}

SENSITIVE_RE = re.compile(
    r"password|passwd|pwd|secret|token|access[_-]?key|client_secret|AKIA|Bearer|账号|密码",
    re.I,
)


def should_skip(path: Path) -> bool:
    return any(part in EXCLUDED_DIRS for part in path.parts)


def iter_files(project: Path):
    for root, dirs, files in os.walk(project):
        dirs[:] = [item for item in dirs if item not in EXCLUDED_DIRS and not item.startswith(".")]
        root_path = Path(root)
        for file_name in files:
            yield root_path / file_name


def iter_dirs(project: Path):
    for root, dirs, _files in os.walk(project):
        dirs[:] = [item for item in dirs if item not in EXCLUDED_DIRS and not item.startswith(".")]
        root_path = Path(root)
        for dir_name in dirs:
            yield root_path / dir_name


def rel(path: Path, base: Path = CETC_ROOT) -> str:
    return path.relative_to(base).as_posix()


def find_git_projects() -> list[Path]:
    projects = []
    for git_dir in CETC_ROOT.rglob(".git"):
        if any(part in EXCLUDED_DIRS - {".git"} for part in git_dir.parent.relative_to(CETC_ROOT).parts):
            continue
        projects.append(git_dir.parent)
    return sorted(projects)


def read_text(path: Path, max_chars: int = 1200) -> str:
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return ""
    text = re.sub(r"\s+", " ", text).strip()
    return text[:max_chars]


def first_existing(project: Path, names: tuple[str, ...]) -> Path | None:
    for name in names:
        candidate = project / name
        if candidate.exists():
            return candidate
    return None


def collect_files(project: Path, patterns: tuple[str, ...], limit: int = 30) -> list[str]:
    items = []
    suffix_patterns = [pattern.replace("*", "") for pattern in patterns if pattern.startswith("*")]
    exact_patterns = [pattern for pattern in patterns if not pattern.startswith("*")]
    for path in iter_files(project):
        if path.name in exact_patterns or any(path.name.endswith(pattern) for pattern in suffix_patterns):
            items.append(path)
    unique = sorted({rel(path, project) for path in items})
    return unique[:limit]


def collect_dirs(project: Path, names: tuple[str, ...], limit: int = 30) -> list[str]:
    items = []
    for path in iter_dirs(project):
        if path.name in names:
            items.append(path)
    unique = sorted({rel(path, project) for path in items})
    return unique[:limit]


def parse_package(path: Path | None) -> dict[str, object]:
    if not path:
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    dependencies = sorted((data.get("dependencies") or {}).keys())
    dev_dependencies = sorted((data.get("devDependencies") or {}).keys())
    return {
        "name": data.get("name", ""),
        "description": data.get("description", ""),
        "scripts": sorted((data.get("scripts") or {}).keys()),
        "dependenciesSample": dependencies[:12],
        "devDependenciesSample": dev_dependencies[:12],
    }


def parse_pom(path: Path | None) -> dict[str, str]:
    if not path:
        return {}
    text = path.read_text(encoding="utf-8", errors="ignore")
    def tag(name: str) -> str:
        match = re.search(rf"<{name}>\s*([^<]+)\s*</{name}>", text)
        return match.group(1).strip() if match else ""
    return {"groupId": tag("groupId"), "artifactId": tag("artifactId"), "name": tag("name"), "description": tag("description")}


def config_files(project: Path) -> list[str]:
    results = []
    for path in iter_files(project):
        name = path.name
        if name in CONFIG_NAMES or name.startswith(".env") or "config" in name.lower() and path.suffix in {".js", ".json", ".ts"}:
            results.append(rel(path, project))
    return sorted(set(results))[:40]


def sensitive_files(project: Path) -> list[str]:
    results = []
    for path in iter_files(project):
        if path.suffix.lower() not in {".js", ".vue", ".json", ".yml", ".yaml", ".properties", ".md", ".java", ".ts"}:
            continue
        try:
            sample = path.read_text(encoding="utf-8", errors="ignore")[:4000]
        except OSError:
            continue
        if SENSITIVE_RE.search(sample):
            results.append(rel(path, project))
    return sorted(set(results))[:30]


def infer_action(relative_project: str) -> str:
    if relative_project in ACTION_RULES:
        return ACTION_RULES[relative_project]
    if relative_project.startswith(HIGH_VALUE_PREFIXES) or relative_project in HIGH_VALUE_NAMES:
        return "保留到抽取完成"
    return "归档"


def infer_value(relative_project: str) -> str:
    if relative_project.startswith("cgpt2.0/"):
        return "城市治理业务链"
    if relative_project.startswith("xinfang/"):
        return "信访业务链"
    if relative_project.startswith("gis/") or relative_project in {"jun-dd-web", "cetc-ui/bi-ui"}:
        return "GIS / BI / 地图资产"
    if relative_project.startswith("1.2-project-network-security"):
        return "网络安全业务"
    if relative_project.startswith("smartCity/"):
        return "智慧城市业务"
    if relative_project in {"brain", "BeijingDaxing/cetc-moniwa-ui"}:
        return "监测预警 / 大屏"
    return "低到中，需按目录确认"


def summarize_project(project: Path) -> dict[str, object]:
    relative_project = rel(project)
    readme = first_existing(project, ("README.md", "README.MD", "README.zh-CN.md"))
    package = first_existing(project, ("package.json",))
    pom = first_existing(project, ("pom.xml",))
    pages = collect_files(project, ("*.vue",), 25)
    api_files = [item for item in collect_files(project, ("*.js", "*.ts"), 80) if "/api/" in f"/{item}" or item.startswith("api/")][:25]
    backend = collect_files(project, ("*Controller.java", "*Service.java", "*Mapper.java"), 35)
    dirs = collect_dirs(project, ("views", "pages", "modules", "components", "api", "router", "store", "controller", "service", "mapper"), 35)
    configs = config_files(project)
    sensitive = sensitive_files(project)
    return {
        "project": relative_project,
        "path": str(project),
        "businessValue": infer_value(relative_project),
        "recommendedAction": infer_action(relative_project),
        "readme": rel(readme, project) if readme else "",
        "readmeSummary": read_text(readme) if readme else "",
        "package": parse_package(package),
        "pom": parse_pom(pom),
        "structureDirs": dirs,
        "pageSamples": pages,
        "apiSamples": api_files,
        "backendSamples": backend,
        "configFiles": configs,
        "sensitiveSignalFiles": sensitive,
        "counts": {
            "pages": len(pages),
            "apiFiles": len(api_files),
            "backendFiles": len(backend),
            "configFiles": len(configs),
            "sensitiveSignalFiles": len(sensitive),
        },
    }


def bullet_list(items: list[str], empty: str = "未发现", limit: int = 8) -> str:
    if not items:
        return f"- {empty}\n"
    lines = [f"- `{item}`" for item in items[:limit]]
    if len(items) > limit:
        lines.append(f"- ... 另有 {len(items) - limit} 项")
    return "\n".join(lines) + "\n"


def render_markdown(report: dict[str, object]) -> str:
    projects = report["projects"]
    action_counts = Counter(project["recommendedAction"] for project in projects)
    lines = [
        "---",
        "title: CETC 自动资产抽取报告",
        "tags: [reference, code, cetc, archive, generated]",
        f"created: {report['date']}",
        "source: /Users/cuizihao/CETC/Project",
        "related: [CETC 删除前资产抽取清单, CETC 旧项目业务价值与架构判断]",
        "---",
        "",
        "# CETC 自动资产抽取报告",
        "",
        f"> 生成时间：{report['generatedAt']}",
        "",
        "## 总览",
        "",
        f"- 扫描项目：{len(projects)} 个",
        f"- JSON 输出：`outputs/cetc-asset-extraction.json`",
        f"- Markdown 输出：`outputs/cetc-asset-extraction.md`",
        "",
        "| 建议动作 | 数量 |",
        "| --- | ---: |",
    ]
    for action, count in sorted(action_counts.items()):
        lines.append(f"| `{action}` | {count} |")

    lines.extend(
        [
            "",
            "## 清理优先级",
            "",
            "| 项目 | 业务价值 | 建议动作 | 配置线索 | 敏感线索 |",
            "| --- | --- | --- | ---: | ---: |",
        ]
    )
    for project in projects:
        counts = project["counts"]
        lines.append(
            f"| `{project['project']}` | {project['businessValue']} | `{project['recommendedAction']}` | "
            f"{counts['configFiles']} | {counts['sensitiveSignalFiles']} |"
        )

    lines.extend(["", "## 项目明细", ""])
    for project in projects:
        package = project["package"]
        pom = project["pom"]
        lines.extend(
            [
                f"### {project['project']}",
                "",
                f"- 业务价值：{project['businessValue']}",
                f"- 建议动作：`{project['recommendedAction']}`",
                f"- README：`{project['readme'] or '未发现'}`",
                f"- 前端页/组件样本数：{project['counts']['pages']}",
                f"- API 文件样本数：{project['counts']['apiFiles']}",
                f"- 后端 Controller/Service/Mapper 样本数：{project['counts']['backendFiles']}",
                f"- 配置文件线索数：{project['counts']['configFiles']}",
                f"- 敏感关键词线索数：{project['counts']['sensitiveSignalFiles']}",
                "",
            ]
        )
        if package:
            lines.append(f"- package：`{package.get('name') or '未命名'}`，脚本：`{', '.join(package.get('scripts', [])) or '无'}`")
        if pom:
            pom_name = pom.get("name") or pom.get("artifactId") or "未命名"
            lines.append(f"- Maven：`{pom_name}`")
        if project["readmeSummary"]:
            lines.extend(["", "README 摘要：", "", f"> {project['readmeSummary'][:450]}"])

        lines.extend(["", "关键目录：", bullet_list(project["structureDirs"])])
        lines.extend(["API 样本：", bullet_list(project["apiSamples"])])
        lines.extend(["后端样本：", bullet_list(project["backendSamples"])])
        lines.extend(["配置线索：", bullet_list(project["configFiles"])])
        lines.extend(["敏感关键词线索：", bullet_list(project["sensitiveSignalFiles"])])
    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    generated_at = datetime.now(timezone.utc).isoformat()
    projects = [summarize_project(project) for project in find_git_projects()]
    report = {
        "generatedAt": generated_at,
        "date": datetime.now().date().isoformat(),
        "source": str(CETC_ROOT),
        "projects": projects,
    }
    OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)
    JSON_PATH.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    markdown = render_markdown(report)
    MD_PATH.write_text(markdown, encoding="utf-8")
    REFERENCE_PATH.write_text(markdown, encoding="utf-8")
    print(f"Generated {len(projects)} CETC asset records.")
    print(f"Wrote {JSON_PATH.relative_to(ROOT)}")
    print(f"Wrote {REFERENCE_PATH.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
