#!/usr/bin/python3
"""
This module sends a POST request to a specified URL
with an email as a parameter and displays the response body.
"""
from urllib.request import urlopen, Request
from urllib.parse import urlencode
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    data = urlencode({"email": email}).encode("utf-8")
    req = Request(url, data=data)

    with urlopen(req) as response:
        body = response.read()

    print(body.decode("utf-8"))
