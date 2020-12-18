#module file: ask.py

"""This module receives an array, dictionary or a string of
configuration variable(s). Converts it to dictionary if not and prompts user to
provide values for each parameter by printing the questions and reading the
answers given by the user."""

from . import prepare

def ask(questions):
    prepared_q = prepare(questions)
    for q, a in prepared_q.items():
        a = input("What's the " + str(q) + " ?  ")
        prepared_q[q] = a
    return prepared_q


