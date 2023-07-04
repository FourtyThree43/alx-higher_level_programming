#!/usr/bin/python3
"""
This script communicates with the github API commits endpoint
and gets the sha and author name of the last ten commits
"""
import requests
from sys import argv


def get_commits_github(repo: str, owner: str):
    """The password is the personal access token"""

    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)

    """The github api recommands that the 'Accept' header
        be specified
    """
    headers = {"Accept": "application/vnd.github+json"}
    req = requests.get(url, headers=headers)

    # the response content is deserialized
    list_commits = req.json()

    i = 0
    while i < 10:
        commit_dict = list_commits[i]
        name = commit_dict.get("commit").get("author").get("name")
        sha = commit_dict.get("sha")
        print("{}: {}".format(sha, name))

        i += 1


if __name__ == "__main__":
    try:
        repository = argv[1]
        owner = argv[2]
        get_commits_github(repository, owner)
    except IndexError:
        pass
