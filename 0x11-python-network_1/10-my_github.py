#!/usr/bin/python3
"""takes your GitHub credentials
and uses the GitHub API to display your id
"""
import requests as r
from sys import argv


if __name__ == "__main__":
    cred = (argv[1], argv[2])
    res = r.get("https://api.github.com/user", verify=False, auth=cred)
    if "id" in res.json():
        print(res.json().get("id"))
    else:
        print("None")
