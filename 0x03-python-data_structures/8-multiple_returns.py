#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        sentence[0] = None
    a = len(sentence), sentence[0]
    return a
