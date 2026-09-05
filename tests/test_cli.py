"""Verify the installed CLI's public behavior."""

from importlib.metadata import version

import pytest

from agent_harness_lab.cli import main


def test_no_arguments_shows_help(capsys: pytest.CaptureFixture[str]) -> None:
    main([])
    assert "usage: agent-harness-lab" in capsys.readouterr().out


def test_version_matches_installed_distribution(capsys: pytest.CaptureFixture[str]) -> None:
    with pytest.raises(SystemExit) as error:
        main(["--version"])
    assert error.value.code == 0
    assert capsys.readouterr().out.strip() == version("agent-harness-lab")


def test_unknown_option_is_rejected() -> None:
    with pytest.raises(SystemExit) as error:
        main(["--unknown-option"])
    assert error.value.code == 2
