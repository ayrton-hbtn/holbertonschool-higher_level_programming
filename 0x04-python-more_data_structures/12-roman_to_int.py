#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) is not str:
        return 0
    roman_values = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500, 
            'M':1000
            }
    res = 0
    for letter in roman_string:
        res += roman_values.get(letter, 0)
    return res
