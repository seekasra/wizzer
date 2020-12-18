#module file: ask.py
from . import prepare

def ask(questions):
    questions = prepare(questions)
    for q, a in questions.items():
        a = input("What's the " + str(q) + " ?  ")
        questions[q] = a
    return questions


name = "wizer.py"
description = "wizer.py is a Wizard question answer creator for seting up variables/configurations " 

