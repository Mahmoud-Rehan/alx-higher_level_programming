#!/usr/bin/python3
""" Python script that takes in a URL,
    sends a request to the URL and displays
    the body of the response. """
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]

    request = requests.get(url)

    if request.status_code >= 400:
        print(f"Error code: {request.status_code}")
    else:
        print(request.text)
