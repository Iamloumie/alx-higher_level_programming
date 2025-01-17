#!/usr/bin/python3
"""A python script that:
- takes in a URL
- sends a request to the URL and displays
- the body of the response(decoded in utf-8) (ERROR CODE)
- using the requests and sys python packages
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
