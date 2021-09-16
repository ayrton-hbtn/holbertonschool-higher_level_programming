#!/usr/bin/python
def weight_average(my_list=[]):
    if not my_list:
        return 0
    num = 0
    den = 0
    for t in my_list:
        num += t[0] * t[1]
        den += t[1]
    return (num / den)
