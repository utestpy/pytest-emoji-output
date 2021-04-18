![Screenshot](media/icon.png)

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Build Status](https://travis-ci.org/vyahello/pytest-emoji-output.svg?branch=master)](https://travis-ci.org/vyahello/pytest-emoji-output)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE.md)
[![PyPI version shields.io](https://img.shields.io/pypi/v/pytest-emoji-output.svg)](https://pypi.org/project/pytest-emoji-output/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/pytest-emoji-output.svg)](https://pypi.org/project/pytest-emoji-output/)
[![PyPi downloads](https://img.shields.io/pypi/dm/pytest-emoji-output.svg)](https://pypi.python.org/pypi/pytest-emoji-output)
[![Downloads](https://pepy.tech/badge/pytest-emoji-output)](https://pepy.tech/project/pytest-emoji-output)
[![Docs](https://img.shields.io/badge/docs-github-orange)](https://vyahello.github.io/pytest-emoji-output/)

# Pytest emoji output

> A pytest plugin that helps to reflect tests output with emoji. 

## Tools

### Production
- python 3.6, 3.7, 3.8
- [pytest](https://pypi.org/project/pytest/)

### Development
- [travis](https://travis-ci.org/)
- [black](https://black.readthedocs.io/en/stable/)
- [mypy](https://mypy.readthedocs.io/en/latest)
- [pylint](https://www.pylint.org/)
- [flake8](http://flake8.pycqa.org/en/latest/)
- [interrogate](https://interrogate.readthedocs.io/en/latest/)

## Usage

![Demo](media/howto.gif)

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

**[⬆ back to top](#pytest-emoji-output)**

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
* [https://twitter.com/vyahello](https://twitter.com/vyahello)
* [https://www.linkedin.com/in/volodymyr-yahello-821746127](https://www.linkedin.com/in/volodymyr-yahello-821746127)

### Contributing
I would highly appreciate any contribution and support. If you are interested to add your ideas into project please follow next simple steps:

1. Clone the repository
2. Configure `git` for the first time after cloning with your `name` and `email`
3. `pip install -r requirements.txt` to install all project dependencies
4. `pip install -r requirements-dev.txt` to install all development project dependencies
5. Create your feature branch (`git checkout -b feature/fooBar`)
6. Commit your changes (`git commit -am 'Add some fooBar'`)
7. Push to the branch (`git push origin feature/fooBar`)
8. Create a new Pull Request

### What's next

All recent activities and ideas are described at project [issues](https://github.com/vyahello/pytest-emoji-output/issues). 
If you have ideas you want to change/implement please do not hesitate and create an issue.

**[⬆ back to top](#pytest-emoji-output)**
