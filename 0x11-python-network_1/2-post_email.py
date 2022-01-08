#!/usr/bin/python3
""" sends a POST request to the passed URL with the email as a parameter """

from urllib import request as r, parse as p
from sys import argv

email = {"email": argv[2]}
data = p.urlencode(email).encode()
req = r.Request(argv[1], data)
with r.urlopen(req) as res:
    content = res.read()
print(content.decode('utf-8'))
