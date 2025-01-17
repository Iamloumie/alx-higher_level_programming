#!/usr/bin/python3
"""A python script that:
- takes in a URL and an email
- sends a POST request to the passed URL with email as parameter
- and displays the body of the response(decoded in utf-8)
"""

import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({"email": email}).encode("ascii")

    output = urllib.request.Request(url, data)
    with urllib.request.urlopen(output) as response:
        print(response.read().decode("utf-8"))
