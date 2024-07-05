#!/usr/bin/python3
""" Python script that fetches
    https://alx-intranet.hbtn.io/status """
from urllib.request import urlopen


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with urlopen(url) as response:
        body = response.read()

    body_type = type(body)
    decoded = body.decode("utf-8")
    print(f"Body response:")
    print(f"\t- type: {body_type}")
    print(f"\t- content: {body}")
    print(f"\t- utf8 content: {decoded}")
