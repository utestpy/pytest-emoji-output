"""Module contains main API to work with pytest-emoji-output plugin."""
import sys
from typing import Tuple
from _pytest.config import Config
from _pytest.config.argparsing import Parser, OptionGroup
from _pytest.reports import TestReport


def pytest_addoption(parser: Parser) -> None:
    """Turns on emoji parser feature.

    Args:
        parser (Parser): cli parser
    """
    group: OptionGroup = parser.getgroup("emoji")
    group.addoption("--emoji", "-j", action="store_true", help="Adds emoji to pytest results")


def pytest_report_header(config: Config) -> str:  # type: ignore
    """Adds header to pytest runner.

    Args:
        config (Config): configuration option
    """
    if config.getoption("emoji"):
        return f"Running on {sys.platform} platform: {'{}.{}.{}'.format(*sys.version_info[:3])} python version"


def pytest_report_teststatus(report: TestReport, config: Config) -> Tuple[str, str, str]:  # type: ignore
    """Turn failures into opportunities.

    Args:
        report (TestReport): pytest report item
        config (Config): pytest configuration item
    """
    if report.when == "call":
        if report.passed and config.getoption("emoji"):
            return report.outcome, "😇", "😇 Yes sir, it is passed"
        if report.failed and config.getoption("emoji"):
            return report.outcome, "😡", "😡 Oh crap, it is failed"
