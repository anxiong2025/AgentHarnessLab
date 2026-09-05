"""Offline tool checks for lesson 01; no API key required."""

import json
from pathlib import Path
from tempfile import TemporaryDirectory

from agent_harness_lab.first_agent import execute_tool

with TemporaryDirectory() as temp:
    root = Path(temp).resolve()
    (root / "README.md").write_text("lesson fixture", encoding="utf-8")
    success = json.loads(execute_tool(root, "read_file", '{"path":"README.md"}', 100, 10))
    assert success["ok"] is True
    assert success["text"] == "lesson fixture"
    for arguments in [
        '{"path":"missing.txt"}',
        '{"path":"../outside.txt"}',
        '{"path":123}',
        "not-json",
    ]:
        result = json.loads(execute_tool(root, "read_file", arguments, 100, 10))
        assert result["ok"] is False, arguments
    oversized = json.loads(execute_tool(root, "read_file", '{"path":"README.md"}', 2, 10))
    assert oversized["ok"] is False
print("工具读取与拒绝路径检查通过")
