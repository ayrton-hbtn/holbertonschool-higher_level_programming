#!/usr/bin/python3
""" fetches with 'requests' package
"""


import requests


if __name__ == "__main__":
    url_req = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(url_req.text)))
    print("\t- content: {}".format(url_req.text))
