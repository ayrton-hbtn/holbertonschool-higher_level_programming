#!/usr/bin/python3
for c in range(97, 123):
	res = 97 + 122 - c
	if c % 2 == 0:
		res -= 32
	print("{}".format(chr(res)), end="")
