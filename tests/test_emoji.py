import pytest
from attr.exceptions import FrozenInstanceError
from plugin.emoji import _TestStatus, _Emoji


@pytest.fixture(scope="module")
def status() -> _TestStatus:
    return _TestStatus("fake", "short", "long")


def test_outcome(status: _TestStatus) -> None:
    assert status.outcome == "fake"


def test_set_outcome(status: _TestStatus) -> None:
    with pytest.raises(FrozenInstanceError):
        status.outcome = None


def test_short(status: _TestStatus) -> None:
    assert status.short == "short"


def test_set_short(status: _TestStatus) -> None:
    with pytest.raises(FrozenInstanceError):
        status.short = None


def test_long(status: _TestStatus) -> None:
    assert status.long == "long"


def test_set_long(status: _TestStatus) -> None:
    with pytest.raises(FrozenInstanceError):
        status.long = None


def test_emoji() -> None:
    assert str(_Emoji.HOLY) == '😇'
    assert str(_Emoji.HELLISH) == '😡'
