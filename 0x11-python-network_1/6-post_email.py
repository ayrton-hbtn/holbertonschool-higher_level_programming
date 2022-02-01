#!/usr/bin/python3
""" Python script
"""


import sys
import requests


if __name__ == "__main__":
    url_request = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(url_request.text)
