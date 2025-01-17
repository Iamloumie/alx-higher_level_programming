#!/usr/bin/python3
"""Python script that takes in URL:
- sends a POST request to the http://0.0.0.0:5000/search_user (THE URL)
- taking the letter as the parameter
- using the sys and requests python packages
"""

import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) == 1:
        letter = ""
    else:
        letter = sys.argv[1]

    q_data = {"q": letter}
    req = requests.post("http://0.0.0.0:5000/search_user", data=q_data)

    try:
        response = req.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
