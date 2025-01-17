#!/usr/bin/python3
"""Python script that sends a POST request to search for a user
- based on a letter
"""

import sys
import requests


if __name__ == "__main__":
    # If no argument is provided, use empty string,
    # Otherwise take first argument
    q = "" if len(sys.argv) < 2 else sys.argv[1]

    # Send POST requests with the letter parameter
    url = sys.argv[1]
    payload = {"q": q}

    try:
        response = requests.post(url, data=payload)

        # Try to parse JSON response
        try:
            json_response = response.json()

            # check if the response is empty
            if json_response:
                print(
                    "[{}] {}".format(json_response.get("id"), json_response.get("name"))
                )
            else:
                print("No result")
        except ValueError:
            print("Not a valid JSON")

    except requests.exceptions.RequestException:
        print("No result")
