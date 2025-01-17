#!/usr/bin/python3
"""A python script that:
- takes in a URL
- sends a request to the URL and displays
- the value of the X-request-ID variable found in the header response
"""

import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    req = urllib.request.Request(url)
    with urllib.request.urlopen(request) as resp:
        print(dict(resp.headers).get("X-Request-Id"))
