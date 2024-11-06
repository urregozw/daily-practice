#!/usr/bin/python3

# Exercise 1.6 from CiCt
# By @urregozw


def string_compression(s: str) -> str:
    """
        There is no String Builder construct in Python as it
        P = lenght of the string
        K = number of character sequences
        T.C: O(P + k^2)
        S.C: O(P)
    """
    h = {}

    for letter in s:
        if letter in h:
            h[letter] += 1
        else:
            h[letter] = 1
    
    substring = ""
    for letter in s:
        if letter in h:
            substring += letter + str(h[letter])
            del h[letter]
    

    return substring if len(substring) < len(s) else s




print(string_compression("a"))
            