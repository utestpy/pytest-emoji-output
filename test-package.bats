#!/usr/bin/env bats


setup() {
:<<DOC
  Installs emoji package
DOC
  python setup.py install
}


teardown() {
:<<DOC
  Removes emoji package
DOC
  rm -rf ${PACKAGE_NAME}.egg-info dist build
}


@test "package name" {
:<<DOC
  Test package name
DOC
  pip list | grep ${PACKAGE_NAME}
  [ "$?" -eq 0 ]
}


@test "package version" {
:<<DOC
  Test package version
DOC
  pip list | grep ${PACKAGE_VERSION}
  [ "$?" -eq 0 ]
}


@test "pytest help message" {
:<<DOC
  Test pytest help message
DOC
  pytest --help | grep "Adds emoji to pytest results"
  [ "$?" -eq 0 ]
}


@test "pytest long flag" {
:<<DOC
  Test pytest long flag
DOC
  pytest --help | grep "emoji-out"
  [ "$?" -eq 0 ]
}


@test "pytest short flag" {
:<<DOC
  Test pytest short flag
DOC
  pytest --help | grep "eo"
  [ "$?" -eq 0 ]
}
