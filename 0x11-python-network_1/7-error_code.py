#!/usr/bin/python3
""" Python script
"""


import sys
import requests


if __name__ == "__main__":
    url_req = requests.get(sys.argv[1])
    if url_req.status_code >= 400:
        print("Error code: {}".format(url_req.status_code))
    else:
        print(url_req.text)
