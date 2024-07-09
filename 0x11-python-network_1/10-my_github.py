#!/usr/bin/python3
""" Python script that takes your
    GitHub credentials (username
    and password) and uses the GitHub
    API to display your id """
import requests
import requests.auth import HTTPBasicAuth
from sys import argv


if __name__ == "__main__":
    auth = HTTPBasicAuth(argv[1], argv[2])
    request = requests.get("https://api.github.com/user", auth=auth)
    print(request.json().get("id"))
