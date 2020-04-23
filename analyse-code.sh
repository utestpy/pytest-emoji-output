#!/usr/bin/env bash

PACKAGE="plugin"


entry-point-box() {
:<<DOC
    Provides pretty-printer check box
DOC
    printf "Start ${1} analysis ...\n"
}


remove-pycache() {
:<<DOC
    Removes python cache directories
DOC
    ( find . -d -name __pycache__ | xargs rm -r )
}


check-black() {
:<<DOC
    Runs "black" code analyser
DOC
    entry-point-box "black" && ( black --check ${PACKAGE} )
}


check-flake() {
:<<DOC
    Runs "flake8" code analyser
DOC
    entry-point-box "flake" && ( flake8 ${PACKAGE} )
}

check-pylint() {
:<<DOC
    Runs "pylint" code analyser
DOC
    entry-point-box "pylint" && ( pylint $(find ./ -iname *.py) )
}


check-mypy() {
    :<<DOC
    Runs "mypy" code analyser
DOC
    entry-point-box "mypy" && ( mypy --package ${PACKAGE} )
}


check-unittests() {
:<<DOC
    Runs unittests using "pytest" framework
DOC
    entry-point-box "unitests" && pytest
}


main() {
:<<DOC
    Runs "main" code analyser
DOC
    remove-pycache
    check-black && check-mypy && check-flake && check-pylint && check-unittests
}


main