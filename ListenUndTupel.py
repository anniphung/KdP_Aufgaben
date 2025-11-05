#Blatt 2 Aufgabe 2, Listen und Tupel

from rezeptListe import rezepte

print(rezepte, '\n','------------------------------------------', '\n')

rezepteFingerfood = []
zutaten = []
einkaufsliste = []

#a)
#ich habe keine Ahnung wie man hier sinnvoll eine while-Loop einsetzen soll, daher habe ich einfach die for loop in eine while-Loop umgeschrieben?????

'''for x in rezepte:
  if x[0] == 'fingerfood':
    rezepteFingerfood.append(x)
    print(rezepteFingerfood, '\n', '====', '\n')

print('alle fingerfood rezepte gefunden')'''

i = 0 

while i < len(rezepte):
  if rezepte[i][0] == 'fingerfood':
    rezepteFingerfood.append(rezepte[i])
    print(rezepteFingerfood, '\n', '====', '\n')
    i += 1
  else:
    i += 1

print('alle fingerfood rezepte gefunden')


#b)

for rezept in rezepteFingerfood:   #iteriert über alle rezepte mit dem schlagwort fingerfood (in der in a )
  for zutat in rezept[1]:
    if not (zutat[1] in zutaten):
      zutaten.append(zutat[1])
      print(zutaten,  '\n', '====', '\n')

#c)
index=0
for zutat in zutaten:
  index += 1
  menge = 0
  for rezept in rezepteFingerfood:
    for rezeptZutat in rezept[1]:
      if rezeptZutat[1] == zutat:
        menge += rezeptZutat[0]
        print(menge, zutat)
  einkaufsliste.append((menge, zutat))
  print(einkaufsliste, '\n', '-------------------', '\n') 
  #suche nach allen einträgen in rezepteFingerfood, die die zutat x verwenden 

print('Einkaufsliste: ', einkaufsliste)