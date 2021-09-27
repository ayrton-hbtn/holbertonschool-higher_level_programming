#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    a = 0
    for i in my_list:
        if a == x:
            break
        try:
            print("{}".format(i), end="")
        except IndexError:
            pass
        a += 1
    print("")
    return x
