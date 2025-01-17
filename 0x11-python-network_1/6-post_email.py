#!/usr/bin/python3
"""A python script that:
- takes in a URL and an email
- sends a POST request to the passed URL with email as parameter
- and displays the body of the response(decoded in utf-8)
- using the requests and sys python packages
"""

import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    email = {"email": sys.argv[2]}

    req = requests.post(url, data=email)
    print(req.text)
