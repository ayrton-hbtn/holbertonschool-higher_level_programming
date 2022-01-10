#!/usr/bin/python3
""" fetches with 'requests' package
"""

from requests import get

if __name__ == "__main__":
    data = get('https://intranet.hbtn.io/status')
    print("Body response:")
    print('\t- type: {}'.format(type(data.text)))
    print('\t- content: {}'.format(data.text))
