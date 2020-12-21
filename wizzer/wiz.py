from . import convert
class Wiz:
  def ask(questions):
      dict_q = convert(questions)
      for q, a in dict_q.items():
          a = input("What's the " + str(q) + " ?  ")
          dict_q[q] = a
      return dict_q
