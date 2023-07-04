#!/usr/bin/python3
"""
This module fetches the status from a url.
"""
from urllib.request import urlopen, Request

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    req = Request(url)

    with urlopen(req) as response:
        body = response.read()

    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(body.decode("utf-8")))
