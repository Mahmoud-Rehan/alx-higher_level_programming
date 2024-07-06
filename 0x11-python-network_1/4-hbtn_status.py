#!/usr/bin/python3
""" Python script that
    fetches https://alx-intranet.hbtn.io/status """
import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    request = requests.get(url)
    request_type = type(request.text)

    print("Body response:")
    print(f"\t- type: {request_type}")
    print(f"\t- content: {request.text}")
