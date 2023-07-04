#!/usr/bin/python3
"""
This module sends a request to a specified URL and
displays the value of the X-Request-Id header.
using the requests package.
"""
import requests
from sys import argv

if __name__ == "__main__":
    url: str = argv[1]

    req = requests.get(url)
    header = req.headers.get("X-Request-Id")

    print(header)
