"""Contains API for pytest-emoji plugin."""
import sys
from typing import Tuple
from _pytest.config import Config
from _pytest.config.argparsing import Parser
from _pytest.reports import TestReport


def pytest_addoption(parser: Parser) -> None:
    """Turns on emoji parser feature.

    Args:
        parser: cli parser
    """
    group = parser.getgroup("emoji")
    group.addoption("--emoji", action="store_true", help="Adds emoji to pytest results")


def pytest_report_header(config: Config) -> str:
    """Adds header tp pytest runner.

    Args:
        config: configuration option
    """
    if config.getoption("emoji"):
        return f"Running on {sys.platform} platform: {'{}.{}.{}'.format(*sys.version_info[:3])} python version"


def pytest_report_teststatus(report: TestReport, config: Config) -> Tuple[str, str, str]:
    """Turns on report status modification.

    Args:
        report: testcase report
        config: configuration option
    """
    if report.when == "call":
        if report.passed and config.getoption("emoji"):
            return report.outcome, "😇", "😇 Yes sir, it is passed"
        if report.failed and config.getoption("nice"):
            return report.outcome, "😡", "😡  Oh crap, it is failed"
