#!/usr/bin/python3

def find_peak(list_of_integers):
    """ that finds a peak in a list of unsorted integers """
    if not list_of_integers:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    else:
        peak = find_peak(list_of_integers[1:])
        return peak if peak > list_of_integers[0] else list_of_integers[0]
