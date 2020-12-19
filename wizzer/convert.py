#module file: convert.py

"""This module receives an array, dictionary or a string of
configuration variable(s). Converts it to dictionary if returns."""

def convert(lst):
    if isinstance(lst, list):
        res_dct = {lst[i]: '' for i in range(0, len(lst))}
    elif isinstance(lst, str):
        res_dct = {lst: ''} 
    else:
        res_dct = lst
    return res_dct 
