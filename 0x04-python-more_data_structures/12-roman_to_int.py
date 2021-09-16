#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) is not str:
        return 0
    roman_nums = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }
    res = 0
    for c in range(len(roman_string)):
        if roman_string[c] not in roman_nums.keys():
            return 0
        if (c != (len(roman_string) - 1) and roman_nums.get(roman_string[c])
            < roman_nums.get(roman_string[c + 1])):
                res += roman_nums.get(roman_string[c]) * -1
        else:
            res += roman_nums.get(roman_string[c], 0)
    return res
