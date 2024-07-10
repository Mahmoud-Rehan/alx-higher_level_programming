#!/usr/bin/python3
""" Python script that takes in a URL and an email,
    sends a POST request to the passed URL with
    the email as a parameter, and displays the body of
    the response (decoded in utf-8) """
from urllib.request import urlopen, Request
from urllib.parse import urlencode
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    my_value = {"email": argv[2]}

    encoded = urlencode(my_value).encode("ascii")
    request = Request(url, encoded)

    with urlopen(request) as response:
        body = response.read()
        decoded = body.decode("utf-8")
        print(f"Email: {decoded}")
