#!/usr/bin/python3
"""list 10 commits (from the most recent to oldest)
of the repository "rails" by the user "rails"
"""

import requests as r
from sys import argv


if __name__ == "__main__":
    username = argv[2]
    repo = argv[1]
    url = "https://api.github.com/repos/{}/{}/commits".format(username, repo)
    commits = r.get(url, headers={
                    'Content-Type': 'application/vnd.github.v3+json'})
    commits_json = commits.json()
    try:
        for i in range(10):
            print('{}: {}'.format(commits_json[i].get("sha"),
                                  commits_json[i].get("commit")
                                  .get("author").get("name")))
    except IndexError:
        pass
