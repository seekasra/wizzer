#module file: ask.py

"""This module receives an array, dictionary or a string of
configuration variable(s). Converts it to dictionary if not and prompts user to
provide values for each parameter by printing the questions and reading the
answers given by the user."""

from . import convert

def ask(questions):
    dict_q = convert(questions)
    for q, a in dict_q.items():
        a = input("What's the " + str(q) + " ?  ")
        dict_q[q] = a
    return dict_q


