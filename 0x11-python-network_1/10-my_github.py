#!/usr/bin/python3
"""Python Script that takes user Github credentials (username and password)
- and uses the github API to display user ID
- using the sys and requests python packages
"""

import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    auth = HTTPBasicAuth(username, password)
    req = requests.get("https://api.github.com/user", auth=auth)

    print(req.json().get("id"))
