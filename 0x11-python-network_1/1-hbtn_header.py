#!/usr/bin/python3
"""
This module sends a request to a specified URL and
displays the value of the X-Request-Id header.
"""
from urllib.request import urlopen, Request
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    req = Request(url)

    with urlopen(req) as response:
        header = response.getheader("X-Request-Id")

    print(header)
