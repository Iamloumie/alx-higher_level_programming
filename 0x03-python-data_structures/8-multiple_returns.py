#!/usr/bin/python3

def multiple_returns(sentence):
    size = len(sentence)
    if size > 0:
        first_char = sentence[0]
    else:
        first_char = "None"

    return size, first_char
