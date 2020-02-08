"""Testing the pytest-emoji-output plugin."""
import pytest
from _pytest.pytester import Testdir, RunResult


def test_pass_fail(testdir: Testdir) -> None:
    # create a temporary pytest test module
    testdir.makepyfile(
        """
        def test_pass():
            assert 1 == 1

        def test_fail():
            assert 1 == 2
    """
    )

    # run pytest
    result: RunResult = testdir.runpytest()

    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines(
        ["*.F*",]  # . for Pass, F for Fail
    )

    # make sure that that we get a '1' exit code for the testsuite
    assert result.ret == 1


@pytest.fixture()
def sample_test(testdir: Testdir) -> Testdir:
    testdir.makepyfile(
        """
        def test_pass():
            assert 1 == 1

        def test_fail():
            assert 1 == 2
    """
    )
    return testdir


def test_with_emoji(sample_test: Testdir) -> None:
    result: RunResult = sample_test.runpytest("--emoji")
    result.stdout.fnmatch_lines(
        ["*.O*",]
    )  # . for Pass, O for Fail
    assert result.ret == 1


def test_with_emoji_verbose(sample_test: Testdir) -> None:
    result: RunResult = sample_test.runpytest("-v", "--emoji")
    result.stdout.fnmatch_lines(
        ["*::test_fail OPPORTUNITY for improvement*",]
    )
    assert result.ret == 1


def test_not_emoji_verbose(sample_test: Testdir) -> None:
    result: RunResult = sample_test.runpytest("-v")
    result.stdout.fnmatch_lines(["*::test_fail FAILED*"])
    assert result.ret == 1


def test_header(sample_test: Testdir) -> None:
    result: RunResult = sample_test.runpytest("--emoji")
    result.stdout.fnmatch_lines(["Thanks for running the tests."])


def test_header_not_emoji(sample_test: Testdir) -> None:
    result: RunResult = sample_test.runpytest()
    thanks_message = "Thanks for running the tests."
    assert thanks_message not in result.stdout.str()


def test_help_message(testdir: Testdir) -> None:
    result: RunResult = testdir.runpytest("--help")

    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines(
        ["emoji:", "*--emoji*emoji: turn FAILED into OPPORTUNITY for improvement",]
    )
