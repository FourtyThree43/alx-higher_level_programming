#!/usr/bin/python3
"""
This script communicates with the github API commits endpoint
and gets the sha and author name of the last ten commits
"""
import requests
from sys import argv

if __name__ == "__main__":
    username: str = argv[1]
    access_token: str = argv[2]

    url: str = "https://api.github.com/user"

    response = requests.get(url, auth=(username, access_token))
    status: int = response.status_code

    if status == 200:
        user_id = response.json().get("id")
        print(f"User ID: {user_id}")
    else:
        print(f"Failed to retrieve user ID. Status code: {status}")
