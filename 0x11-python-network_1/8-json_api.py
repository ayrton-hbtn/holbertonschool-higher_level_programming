#!/usr/bin/python3
"""that takes in a letter and sends a POST request
to link in argument
"""
import requests as r
from sys import argv


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    letter = {}
    if len(argv) > 1:
        letter["q"] = argv[1]
    res = r.post(url, data=letter)
    try:
        d = res.json()
        if "id" not in d.get('id') or "name" not in d.get('name'):
            print("No result")
        else:
            print("[{}] {}".format(d.get('id'), d.get('name')))
    except ValueError:
        print("Not a valid JSON")
