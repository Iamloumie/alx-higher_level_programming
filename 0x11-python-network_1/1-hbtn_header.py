#!/usr/bin/python3
"""A python script that:
- takes in a URL
- sends a request to the URL and displays
- the value of the X-request-ID variable found in the header response
"""

import sys
from urllib.request import Request, urlopen

if __name__ == "__main__":
    url = sys.argv[1]
    req = Request(url)

    with urlopen(req) as resp:
        print(dict(resp.headers).get("X-Request-Id"))
