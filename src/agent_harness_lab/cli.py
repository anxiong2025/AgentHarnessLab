"""Command-line entry point for the course package."""

import argparse
from collections.abc import Sequence
from importlib.metadata import version


def main(argv: Sequence[str] | None = None) -> None:
    """Parse CLI arguments and show the available course commands."""
    parser = argparse.ArgumentParser(
        prog="agent-harness-lab",
        description="Agent Harness Lab: build a reliable agent, one lesson at a time.",
    )
    parser.add_argument("--version", action="version", version=version("agent-harness-lab"))
    parser.parse_args(argv)
    parser.print_help()
