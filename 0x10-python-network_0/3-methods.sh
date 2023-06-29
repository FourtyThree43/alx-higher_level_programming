#!/bin/bash
# Takes in a URL and displays all HTTP methods the server will accept.
curl -sI "$1" | perl -ne 'print $1 if /^Allow:\s*(.*)/i'
