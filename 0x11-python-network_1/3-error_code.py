#!/usr/bin/python3
"""A python script that:
- takes in a URL
- sends a request to the URL and displays
- the body of the response(decoded in utf-8)
"""

import sys
from urllib.request import Request, urlopen
import urllib.error


if __name__ == "__main__":
    url = sys.argv[1]

    req = Request(url)
    try:
        with urlopen(req) as response:
            the_page = response.read().decode("utf-8")
            print(the_page)
    except urllib.error.HTTPError as er:
        print("Error code:", er.code)
