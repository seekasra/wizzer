#module file: Wizzer.py

"""This module receives an array, dictionary or a string of
configuration variable(s). Converts it to dictionary if not and prompts user to
provide values for each parameter by printing the questions and reading the
answers given by the user."""

class Wizzer:
    def ask(self, questions):
        dict_q = self._convert(questions)
        for q, a in dict_q.items():
            a = input("What's the " + str(q) + " ?  ")
            dict_q[q] = a
        return dict_q

    def review(self, questions):
        dict_q = self._convert(questions)
        for q, a in dict_q.items():
            print(str(q) + " :  " + str(a))

    def _convert(self, lst):
        if isinstance(lst, list):
            res_dct = {lst[i]: '' for i in range(0, len(lst))}
        elif isinstance(lst, str):
            res_dct = {lst: ''} 
        else:
            res_dct = lst
        return res_dct 
