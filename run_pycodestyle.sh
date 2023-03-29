#!/bin/bash

find . -name '*.py' ! -name '*main*' ! -name '*test*' -exec pycodestyle --show-source {} +


printf "\nCheck Done!\n"
