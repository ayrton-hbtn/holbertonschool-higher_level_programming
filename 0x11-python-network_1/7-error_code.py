#!/usr/bin/python3
""" hola """
import requests as r
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    res = r.get(url)
    if res.status_code >= 400:
        print(f"Error code:{res.status_code}")
    else:
        print(res.request.body)
