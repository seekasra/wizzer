class Wiz:
  def ask(questions):
      dict_q = convert(questions)
      for q, a in dict_q.items():
          a = input("What's the " + str(q) + " ?  ")
          dict_q[q] = a
      return dict_q
    
  def review(questions):
    dict_q = convert(questions)
    for q, a in dict_q.items():
        print(str(q) + " :  " + str(a))
      
  def __convert(lst):
    if isinstance(lst, list):
        res_dct = {lst[i]: '' for i in range(0, len(lst))}
    elif isinstance(lst, str):
        res_dct = {lst: ''} 
    else:
        res_dct = lst
    return res_dct 
