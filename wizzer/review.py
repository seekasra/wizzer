#module file: review.py

"""This module receives an array, dictionary or a string of
configuration variable(s). Converts it to dictionary if not and showes
key/value pairs by printing them out."""

from . import convert

def review(questions):
    dict_q = convert(questions)
    for q, a in dict_q.items():
        print(str(q) + " :  " + str(a))
