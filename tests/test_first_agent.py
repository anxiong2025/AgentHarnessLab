"""Exercise lesson 01 without network requests or model credentials."""

import argparse
import json
from pathlib import Path
from unittest.mock import MagicMock

import pytest
from openai import OpenAI
from openai.types.chat import ChatCompletion

from agent_harness_lab.first_agent import execute_tool, run_agent


def model_response(finish: str, tool: bool = False) -> ChatCompletion:
    """Build an SDK response fixture with a single optional file read."""
    return ChatCompletion.model_validate(
        {
            "id": "fixture",
            "object": "chat.completion",
            "created": 0,
            "model": "fixture",
            "choices": [
                {
                    "index": 0,
                    "finish_reason": finish,
                    "message": {
                        "role": "assistant",
                        "content": None if tool else "Analysis complete",
                        "tool_calls": [
                            {
                                "id": "read-1",
                                "type": "function",
                                "function": {
                                    "name": "read_file",
                                    "arguments": '{"path":"README.md"}',
                                },
                            }
                        ]
                        if tool
                        else None,
                    },
                }
            ],
        }
    )


def options(rounds: int = 2) -> argparse.Namespace:
    """Supply the CLI options used by the loop."""
    return argparse.Namespace(
        task="Read the project",
        model="fixture",
        max_rounds=rounds,
        max_calls_per_round=4,
        max_bytes=100,
        max_entries=10,
    )


@pytest.mark.parametrize(
    "arguments",
    [
        '{"path":"../outside.txt"}',
        '{"path":123}',
        '{"path":"missing.txt"}',
        "not-json",
        '{"path":"README.md","unexpected":true}',
    ],
)
def test_invalid_reads_return_tool_errors(tmp_path: Path, arguments: str) -> None:
    root = tmp_path.resolve()
    result = json.loads(execute_tool(root, "read_file", arguments, 100, 10))
    assert result["ok"] is False


def test_read_limit_rejects_incomplete_file(tmp_path: Path) -> None:
    root = tmp_path.resolve()
    (root / "README.md").write_text("evidence", encoding="utf-8")
    success = json.loads(execute_tool(root, "read_file", '{"path":"README.md"}', 100, 10))
    assert success["text"] == "evidence"
    limited = json.loads(execute_tool(root, "read_file", '{"path":"README.md"}', 2, 10))
    assert limited["ok"] is False
    assert "text" not in limited


def test_loop_pairs_tool_result_with_request(tmp_path: Path) -> None:
    root = tmp_path.resolve()
    (root / "README.md").write_text("fixture evidence", encoding="utf-8")
    client = MagicMock(spec=OpenAI)
    client.chat.completions.create.side_effect = [
        model_response("tool_calls", tool=True),
        model_response("stop"),
    ]
    assert run_agent(client, root, options()) == "Analysis complete"
    messages = client.chat.completions.create.call_args.kwargs["messages"]
    assert messages[-2]["tool_calls"][0]["id"] == "read-1"
    assert messages[-1]["tool_call_id"] == "read-1"
    assert json.loads(messages[-1]["content"])["text"] == "fixture evidence"


@pytest.mark.parametrize("tool", [False, True])
def test_truncated_response_stops_task(tmp_path: Path, tool: bool) -> None:
    client = MagicMock(spec=OpenAI)
    client.chat.completions.create.return_value = model_response("length", tool=tool)
    with pytest.raises(RuntimeError):
        run_agent(client, tmp_path.resolve(), options())
    assert client.chat.completions.create.call_count == 1


def test_round_exhaustion_does_not_report_success(tmp_path: Path) -> None:
    client = MagicMock(spec=OpenAI)
    client.chat.completions.create.return_value = model_response("tool_calls", tool=True)
    with pytest.raises(RuntimeError, match="轮数已耗尽"):
        run_agent(client, tmp_path.resolve(), options(rounds=1))
    assert client.chat.completions.create.call_count == 1
