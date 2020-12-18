#module file: review.py

from . import prepare

def review(questions):
    questions = prepare(questions)
    for q, a in questions.items():
        print(str(q) + " :  " + str(a))
