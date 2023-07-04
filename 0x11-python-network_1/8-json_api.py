#!/usr/bin/python3
"""
This module sends a POST request to http://0.0.0.0:5000/search_user
with a letter as a parameter.
"""

import requests
from sys import argv

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    letter = argv[1] if len(argv) > 1 else ""

    data_d = {"q": letter}

    response = requests.post(url, data=data_d)

    try:
        json_data = response.json()
        if json_data:
            print("[{}] {}".format(json_data.get("id"), json_data.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
