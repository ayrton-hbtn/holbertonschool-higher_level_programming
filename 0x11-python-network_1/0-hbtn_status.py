#!/usr/bin/python3
""" fetches a url and return it's status """
import urllib.request as r


if __name__ == "__main__":
    with r.urlopen('https://intranet.hbtn.io/status') as res:
        print("Body response:")
        content = res.read()
        print(f"\t- type: {type(content)}")
        print(f"\t- content: {content}")
        print(f"\t- utf8 content: {content.decode('utf-8')}")
