#!/usr/bin/python3
"""A python script that:
- takes in a URL (uses the requests and sys packages)
- sends a request to the URL and displays
- the value of the X-request-ID variable found in the header response
"""

import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    req = requests.get(url)
    print(req.headers.get("X-Request-Id"))
