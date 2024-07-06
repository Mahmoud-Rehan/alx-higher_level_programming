#!/usr/bin/python3
""" Python script that list 10 commits
    (from the most recent to oldest)
    of the repository """
import reqests
from sys import argv


if __name__ == "__main__":
    url = f"https://api.github.com/repos/{argv[2]}/{argv[1]}/commits"

    request = requests.get(url)

    json = request.json()

    try:
        for i in range(10):
            sha = json[i].get("sha")
            name = json[i].get("commit").get("author").get("name")
            print(f"{sha}: {name}")
    except IndexError:
        pass
