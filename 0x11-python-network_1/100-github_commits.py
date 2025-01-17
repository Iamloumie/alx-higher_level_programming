#!/usr/bin/python3
"""INTERVIEW TIME:
- ALX staff evaluates candidates applying for a backend position
- question: list 10 commits of the repository 'rails' by the user 'rails'
- using the github API
"""

import sys
import requests


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]

    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)

    req = requests.get(url)
    commits = req.json()
    try:
        for i in range(10):
            print(
                "{}: {}".format(
                    commits[i].get("sha"),
                    commits[i].get("commit").get("author").get("name"),
                )
            )
    except IndexError:
        pass
