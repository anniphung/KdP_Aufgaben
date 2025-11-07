'''
zaehle_elems(xs: list(int), elem: int) -> int
Pre: None
Eff: None
Res: Anzahl
'''


def zaehle_elems(xs, elem):
  if len(xs) == 0:  #Rekursionsanker
    return 0 
  else:             #Rekursionsschritt
    if xs[0] == elem:
      return zaehle_elems(xs[1:], elem) + 1
    else:
      return zaehle_elems(xs[1:], elem)
    

#print(zaehle_elems([1,1,2,3,1,4], 7 ))


'''
count_letters(text:string, wörterbuch: dict)


'''

def count_letters(text, wörterbuch):
  if len(text) == 0: #Rekursionsanker
    return 0
  else:
    return 