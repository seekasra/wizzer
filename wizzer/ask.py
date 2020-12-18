#module file: ask.py

from . import prepare

def ask(questions):
    prepared_q = prepare(questions)
    for q, a in prepared_q.items():
        a = input("What's the " + str(q) + " ?  ")
        prepared_q[q] = a
    return prepared_q


