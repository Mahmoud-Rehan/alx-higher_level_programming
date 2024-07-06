#!/usr/bin/python3
""" Python script that takes in a URL,
    sends a request to the URL and displays
    the body of the response (decoded in utf-8). """
from urllib.request import urlopen, Request
from urllib.parse import urlencode
from urllib.error import HTTPError
from sys import argv


if __name__ == "__main__":
    url = argv[1]

    try:
        request = Request(url)

        with urlopen(request) as response:
            body = respose.read()

        decoded = body.decode("utf-8")
        print(decoded)
    except HTTPError as exception:
        print(f"Error code: {exception.code}")
