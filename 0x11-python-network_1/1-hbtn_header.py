#!/usr/bin/python3
"""a Python script that takes in a
URL and an email,
sends a POST request to the passed URL
with the email as a parameter,
and displays the body of the response
(decoded in utf-8)
"""

from urllib.request import Request, urlopen
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    data = urllib.parse.urlencode(value)
    data = data.encode("ascii")

    req = Request(url, data)
    with urlopen(req) as response:
        the_page = response.read().decode("utf-8")
        print(the_page)
