#!/usr/bin/env zsh
from subprocess import call

call(["git", "submodule", "update"])
