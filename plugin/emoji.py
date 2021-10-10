"""Module contains main API to work with pytest-emoji-output plugin."""
import sys
from enum import Enum
from typing import Tuple, Optional
from _pytest.config import Config
from _pytest.config.argparsing import Parser, OptionGroup
from _pytest.reports import TestReport
from attr import dataclass


class _Emoji(Enum):
    """The class represents an emoji element."""

    HOLY: str = "😇"
    HELLISH: str = "😡"
    SILENT: str = "😶"

    def __str__(self) -> str:
        """Returns emoji string value."""
        return self.value


@dataclass(frozen=True, slots=True)
class _TestStatus:
    """The class represents test status element."""

    outcome: str
    short: str
    long: str


def pytest_addoption(parser: Parser) -> None:
    """Turns on emoji parser feature.

    Args:
        parser (Parser): cli parser
    """
    group: OptionGroup = parser.getgroup("emoji")
    group.addoption(
        "--emoji-out",
        "--eo",
        action="store_true",
        help="Adds emoji to pytest results",
    )


def pytest_report_header(config: Config) -> Optional[str]:  # type: ignore
    """Adds header to pytest runner.

    Args:
        config (Config): configuration option
    """
    if config.getoption("emoji_out"):
        return (
            f"Running on {sys.platform} platform: "
            f"{'{}.{}.{}'.format(*sys.version_info[:3])} python version"
        )


def pytest_report_teststatus(  # type: ignore
    report: TestReport, config: Config
) -> Optional[Tuple[str, str, str]]:
    """Turn failures into opportunities.

    Args:
        report (TestReport): pytest report item
        config (Config): pytest configuration item
    """
    if report.when == "call" and config.getoption("emoji_out"):
        if report.passed:
            passed: _TestStatus = _TestStatus(
                outcome=report.outcome,
                short=str(_Emoji.HOLY),
                long=f"{_Emoji.HOLY} Yes sir, it is passed",
            )
            return passed.outcome, passed.short, passed.long
        if report.failed:
            failed: _TestStatus = _TestStatus(
                outcome=report.outcome,
                short=str(_Emoji.HELLISH),
                long=f"{_Emoji.HELLISH} Oh crap, it is failed",
            )
            return failed.outcome, failed.short, failed.long
        if report.skipped:
            skipped: _TestStatus = _TestStatus(
                outcome=report.outcome,
                short=str(_Emoji.SILENT),
                long=f"{_Emoji.SILENT} Nevermind, it is skipped",
            )
            return skipped.outcome, skipped.short, skipped.long
