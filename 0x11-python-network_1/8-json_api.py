#!/usr/bin/python3
"""Python script that takes in URL:
- sends a POST request to the http://0.0.0.0:5000/search_user (THE URL)
- taking the letter as the parameter
- using the sys and requests python packages
"""

import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    req = requests.get(url)

    if req.status_code >= 400:
        print("Error code:", req.status_code)
    else:
        print(req.text)
