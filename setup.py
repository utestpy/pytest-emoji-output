import os
import codecs
from typing import Sequence, IO
from setuptools import setup


def __read(filename: str) -> str:
    """Reads filename."""
    return codecs.open(os.path.join(os.path.dirname(__file__), filename), encoding="utf-8").read()


def __description() -> str:
    """Returns project description."""
    return __read("README.md")


def __requirements() -> Sequence[str]:
    """Returns requirements sequence."""
    with open("requirements.txt", "r") as requirements:  # type: IO[str]
        return tuple(map(str.strip, requirements.readlines()))


if __name__ == "__main__":
    setup(
        name="pytest-emoji-output",
        version="0.1.0",
        author="Volodymyr Yahello",
        author_email="vyahello@gmail.com",
        maintainer="Volodymyr Yahello",
        maintainer_email="vyahello@gmail.com",
        license="MIT",
        url="https://github.com/vyahello/pytest-emoji-output",
        description="Pytest plugin to represent test output with emoji support",
        long_description=__description(),
        long_description_content_type="text/markdown",
        py_modules=["plugin.emoji"],
        python_requires="!=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, !=3.5.*",
        install_requires=__requirements(),
        classifiers=(
            "Development Status :: 4 - Beta",
            "Framework :: Pytest",
            "Intended Audience :: Developers",
            "Topic :: Software Development :: Testing",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: Implementation :: CPython",
            "Operating System :: OS Independent",
            "License :: OSI Approved :: MIT License",
        ),
        entry_points={"pytest11": ["emoji = plugin.emoji"]},
    )
