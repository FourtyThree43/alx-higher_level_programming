#!/bin/bash

find . -name '*.py' ! -name '*main*' ! -name '*test*' -exec pycodestyle {} +


printf "\nCheck Done!\n"
