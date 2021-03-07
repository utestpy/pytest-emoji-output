#!/usr/bin/env bash


__run_package() {
:<<DOC
  Runs package tests
DOC
  bats --pretty "$1"
}


local() {
:<<DOC
  Runs local package tests
DOC
  __run_package test-package-local.bats
}


remote() {
:<<DOC
  Runs remote package tests
DOC
  __run_package test-package-remote.bats
}


main() {
:<<DOC
  Provides tests runner entrypoint
DOC
  local && remote
}


main