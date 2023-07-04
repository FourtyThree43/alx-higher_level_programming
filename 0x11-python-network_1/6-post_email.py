#!/usr/bin/python3
"""
This module sends a POST request to a specified URL
with an email as a parameter and displays the response body.
using the requests package.
"""
import requests
from sys import argv

if __name__ == "__main__":
    url: str = argv[1]
    email: str = argv[2]
    data_d: dict = {"email": email}

    req = requests.post(url, data=data_d)
    body = req.text

    print(body)
