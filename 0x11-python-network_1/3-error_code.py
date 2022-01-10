#!/usr/bin/python3
"""get error code of url
"""


import sys
from urllib import request as r, error as e


if __name__ == "__main__":
    try:
        with r.urlopen(sys.argv[1]) as f:
            print(f.read().decode('utf-8'))
    except e.HTTPError as err:
        print('Error code: {}'.format(err.code))
