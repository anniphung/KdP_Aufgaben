liste = [2,5,4,1,8,3,6,9,7]

'Spezifikation:'
'Pre: Elemente in Liste haben einen Datentyp, der durch > oder < verglichen und geordnet werden kann'
'Effekt: -'
'Ergebnis: Eine Kopie der Liste in richtiger Reihenfolge wird zurückgegeben'

def bubbleSort(liste: list) -> list:
  liste = liste.copy()
  if liste == []:
    return []
  else:
    i = 0
    while i < len(liste)-1:
      if liste[i] > liste[i+1]:
        temp = liste[i] 
        liste[i] = liste[i+1]
        liste[i+1] = temp
      i += 1
    return bubbleSort(liste[:len(liste)-1]) + [liste[len(liste)-1]]


print(liste)
print(bubbleSort(liste))
