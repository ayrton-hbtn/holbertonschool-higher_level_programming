#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    a = 0
    for i in my_list:
        if x == 0:
            break
        try:
            print("{:d}".format(i), end="")
            a += 1
        except (ValueError, TypeError):
            continue
        x -= 1
    print("")
    return a
