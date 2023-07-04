#!/usr/bin/python3
"""
This module sends a request to a specified URL
and displays the body of the response.
using the requests package.
"""
import requests
from sys import argv

if __name__ == '__main__':
    url: str = argv[1]

    req = requests.get(url)
    status: int = req.status_code
    body = req.text

    if status >= 400:
        print(f"Error code: {status}")
    else:
        print(body)
