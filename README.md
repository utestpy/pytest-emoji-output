![Screenshot](icon.png)

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Build Status](https://travis-ci.org/upymake/pytest-emoji-output.svg?branch=master)](https://travis-ci.org/upymake/pytest-emoji-output)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Forks](https://img.shields.io/github/forks/upymake/pytest-emoji-output)](https://github.com/upymake/pytest-emoji-output/network/members)
[![Stars](https://img.shields.io/github/stars/upymake/pytest-emoji-output)](https://github.com/upymake/pytest-emoji-output/stargazers)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE.md)
[![PyPI version shields.io](https://img.shields.io/pypi/v/pytest-emoji-output.svg)](https://pypi.org/project/pytest-emoji-output/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/pytest-emoji-output.svg)](https://pypi.org/project/pytest-emoji-output/)
[![Downloads](https://pepy.tech/badge/pytest-emoji-output)](https://pepy.tech/project/pytest-emoji-output)

# Pytest emoji output

> A pytest plugin that helps to reflect tests output with emoji. 

## Tools
- python 3.6 | 3.7 | 3.8
- [travis](https://travis-ci.org/) CI
- code analysis
  - [pytest](https://pypi.org/project/pytest/)
  - [black](https://black.readthedocs.io/en/stable/)
  - [mypy](https://mypy.readthedocs.io/en/latest)
  - [pylint](https://www.pylint.org/)
  - [flake8](http://flake8.pycqa.org/en/latest/)

## Usage
> Please click on `gif` file to observe it precisely

![Demo](usage.gif)

### Installation

Please run following script to obtain latest package from PYPI:
```bash
pip install pytest-emoji-output
```

Then please execute command below:
```bash
pytest --emoji-out/--eo <your-tests-directory>
```

### Source code

To be able to use plugin from the source code please execute commands below:
```bash
git clone git@github.com:vyahello/pytest-emoji-output.git
pip install -e .
```

## Development notes

### CI

Project has Travis CI integration using [.travis.yml](.travis.yml) file thus code analysis (`black`, `pylint`, `flake8`) and unittests (`pytest`) will be run automatically
after every made change to the repository.

To be able to run code analysis, please execute command below:
```bash
./analyse-code.sh
```

### Release notes

Please check [changelog](CHANGELOG.md) file to get more details about actual versions and it's release notes.

### Meta

Author – _Volodymyr Yahello_

Distributed under the `MIT` license. See [LICENSE](LICENSE.md) for more information.

You can reach out me at:
* [vyahello@gmail.com](vyahello@gmail.com)
* [https://github.com/vyahello](https://github.com/vyahello)
* [https://www.linkedin.com/in/volodymyr-yahello-821746127](https://www.linkedin.com/in/volodymyr-yahello-821746127)

### Contributing
1. clone the repository
2. configure Git for the first time after cloning with your `name` and `email`
3. `pip install -r requirements.txt` to install all project dependencies
3. `pip install -r requirements-dev.txt` to install all project dev dependencies
