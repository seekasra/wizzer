#module file: wizer.py

def ask(questions):
    questions = prepare(questions)
    for q, a in questions.items():
        a = input("What's the " + str(q) + " ?  ")
        questions[q] = a
    return questions

def review(questions):
    questions = prepare(questions)
    for q, a in questions.items():
        print(str(q) + " :  " + str(a))
        
def prepare(lst):
    if isinstance(lst, list):
        res_dct = {lst[i]: '' for i in range(0, len(lst))}
    elif isinstance(lst, str):
        res_dct = {lst: ''} 
    else:
        res_dct = lst
    return res_dct 


name = "wizer.py"
description = "wizer.py is a Wizard question answer creator for seting up variables/configurations " 

