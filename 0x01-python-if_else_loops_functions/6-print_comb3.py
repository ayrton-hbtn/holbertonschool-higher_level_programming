#!/usr/bin/python3
for i in range(10):
	for j in range(10):
		sep = ", "
		if i == j or i > j:
			continue
		if i != 8:
			print("{}{}{}".format(i, j, sep), end="")
		else:
			print("{}{}".format(i, j))
