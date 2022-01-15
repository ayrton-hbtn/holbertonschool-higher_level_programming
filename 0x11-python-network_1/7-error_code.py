#!/usr/bin/python3
""" sends a request to the URL and displays the body of the response """


import requests as r
from sys import argv


if __name__ == "__main__":
    url = r.get(argv[1])
    if res.status_code >= 400:
        print(f"Error code:{res.status_code}")
    else:
        print(url.request.text)
