#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import shlex
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ASSET_REPORT = ROOT / "outputs" / "cetc-asset-extraction.json"
OUTPUT_JSON = ROOT / "outputs" / "cetc-cleanup-commands.json"
OUTPUT_MD = ROOT / "outputs" / "cetc-cleanup-commands.md"
REFERENCE_MD = ROOT / "30_References" / "cetc-cleanup-command-plan.md"

ARCHIVE_ROOT = Path("/Users/cuizihao/CETC/Archive")
TARGETS = {
    "摘要后可删": ARCHIVE_ROOT / "delete-after-review",
    "归档": ARCHIVE_ROOT / "source-archive",
    "先脱敏后归档": ARCHIVE_ROOT / "sanitize-before-archive",
    "先脱敏后保留": ARCHIVE_ROOT / "sanitize-and-keep",
}


def shell(path: Path | str) -> str:
    return shlex.quote(str(path))


def load_projects() -> list[dict[str, object]]:
    data = json.loads(ASSET_REPORT.read_text(encoding="utf-8"))
    return list(data["projects"])


def build_commands(include_actions: set[str]) -> list[dict[str, str]]:
    commands = []
    for project in load_projects():
        action = str(project["recommendedAction"])
        if action not in include_actions:
            continue
        source = Path(str(project["path"]))
        target_dir = TARGETS[action]
        target = target_dir / source.name
        commands.append(
            {
                "project": str(project["project"]),
                "action": action,
                "businessValue": str(project["businessValue"]),
                "source": str(source),
                "targetDir": str(target_dir),
                "target": str(target),
                "mkdirCommand": f"mkdir -p {shell(target_dir)}",
                "moveCommand": f"mv {shell(source)} {shell(target_dir)}/",
                "status": "planned",
            }
        )
    return commands


def render_markdown(commands: list[dict[str, str]], generated_at: str, include_actions: set[str]) -> str:
    lines = [
        "---",
        "title: CETC 清理命令计划",
        "tags: [reference, code, cetc, cleanup, generated]",
        f"created: {datetime.now().date().isoformat()}",
        "source: /Users/cuizihao/CETC/Project",
        "related: [CETC 清理执行计划, CETC 自动资产抽取报告]",
        "---",
        "",
        "# CETC 清理命令计划",
        "",
        f"> 生成时间：{generated_at}",
        "",
        "## 说明",
        "",
        "这是 dry-run 命令计划，默认不移动、不删除任何项目。",
        "",
        f"- 包含动作：{', '.join(sorted(include_actions))}",
        f"- 命令数量：{len(commands)}",
        f"- JSON 输出：`outputs/cetc-cleanup-commands.json`",
        "",
        "## 目标目录",
        "",
    ]
    for action in sorted(include_actions):
        lines.append(f"- `{action}` -> `{TARGETS[action]}`")

    lines.extend(["", "## 待执行命令", ""])
    for item in commands:
        lines.extend(
            [
                f"### {item['project']}",
                "",
                f"- 业务价值：{item['businessValue']}",
                f"- 建议动作：`{item['action']}`",
                f"- 源目录：`{item['source']}`",
                f"- 目标目录：`{item['targetDir']}`",
                "",
                "```bash",
                item["mkdirCommand"],
                item["moveCommand"],
                "```",
                "",
            ]
        )

    lines.extend(
        [
            "## 执行后复核",
            "",
            "真正移动后，重新运行：",
            "",
            "```bash",
            "python3 scripts/extract-cetc-assets.py",
            "python3 scripts/build-site.py",
            "python3 scripts/build-corpus.py",
            "python3 scripts/build-vector-index.py",
            "```",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate CETC cleanup commands without executing them.")
    parser.add_argument(
        "--include",
        action="append",
        choices=sorted(TARGETS.keys()),
        help="Recommended action category to include. Can be passed multiple times.",
    )
    args = parser.parse_args()

    include_actions = set(args.include or ["摘要后可删"])
    generated_at = datetime.now(timezone.utc).isoformat()
    commands = build_commands(include_actions)
    payload = {
        "generatedAt": generated_at,
        "includeActions": sorted(include_actions),
        "commands": commands,
    }

    OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    markdown = render_markdown(commands, generated_at, include_actions)
    OUTPUT_MD.write_text(markdown, encoding="utf-8")
    REFERENCE_MD.write_text(markdown, encoding="utf-8")
    print(f"Generated {len(commands)} cleanup commands.")
    print(f"Wrote {OUTPUT_JSON.relative_to(ROOT)}")
    print(f"Wrote {REFERENCE_MD.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
