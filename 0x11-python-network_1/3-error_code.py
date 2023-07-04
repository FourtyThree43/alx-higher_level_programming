#!/usr/bin/python3
"""
This module sends a request to a specified URL
and displays the body of the response.
"""
from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError
from sys import argv

if __name__ == '__main__':
    url: str = argv[1]
    req = Request(url)

    try:
        with urlopen(req) as response:
            body = response.read()
        print(body.decode("utf-8"))
    except HTTPError as e:
        print(f"Error code: {e.code}")
