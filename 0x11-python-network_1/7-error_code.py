#!/usr/bin/python3
""" Python script
"""


import sys
import requests


if __name__ == "__main__":
<<<<<<< HEAD
    url = argv[1]
    header = {""}
    res = r.get(url, )
    if res.status_code >= 400:
        print(f"Error code:{res.json}")
=======
    url_req = requests.get(sys.argv[1])
    if url_req.status_code >= 400:
        print("Error code: {}".format(url_req.status_code))
>>>>>>> 85241c4dd80847ae8659238ad4405a79c4bd2989
    else:
        print(url_req.text)
