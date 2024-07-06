#!/usr/bin/python3
""" Python script that takes in a letter
    and sends a POST request to
    http://0.0.0.0:5000/search_user with
    the letter as a parameter. """
import requests
from sys import argv


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"

    if not argv[1]:
        data = {"q": ""}
    else:
        data = {"q": argv[1]}

    response = requests.post(url, data=data)

    try:
        json = response.json()

        if json == {}:
            print("No result")
        else:
            json_id = json.get("id")
            json_name = json.get("name")
            print(f"[{json_id}] {json_name}")
    except Exception:
        print("Not a valid JSON")
