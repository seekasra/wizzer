# -*- coding: utf-8 -*-
"""This module receives an array, dictionary or a string of
configuration variable(s). Converts it to dictionary if not and prompts user to
provide values for each parameter by printing the questions and reading the
answers given by the user."""


def ask(questions):
    """ asking configuration variables from the user """
    dict_q = convert(questions)
    for question, answer in dict_q.items():
        answer = input("What's the " + str(question) + " ?  ")
        dict_q[question] = answer
    return dict_q

def review(questions):
    """ previewing configuration variables from the user """
    dict_q = convert(questions)
    for question, answer in dict_q.items():
        print(str(question) + " :  " + str(answer))


def convert(lst):
    """ converting configuration variables from array and string to
    dictionary """
    if isinstance(lst, list):
        res_dct = {lst[i]: '' for i in range(0, len(lst))}
    elif isinstance(lst, str):
        res_dct = {lst: ''}
    else:
        res_dct = lst
    return res_dct
