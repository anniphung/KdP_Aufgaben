import math

#a)

'''
Signatur:
Eingabe: list(int)
Ausgabe:

Spezifikation:
Voraussetzung:
Effekt:
Ergebnis:
'''

#b)
'''
Signatur:
Eingabe: Integer
Ausgabe: Integer

Spezifikation:
Voraussetzung: Eingabe ist Int
Effekt: - 
Ergebnis: Zahl mit den verliebten Ziffern der Eingabe (Vorzeichen wird erhalten)
'''
zahl = -165702

#i) while
def whileLoved(zahl):
  ergebnis = 0
  whileZahl = abs(zahl)
  i = 0
  while whileZahl > 0:
    if whileZahl%10 != 0:
      ergebnis += (10**i) * (10 - whileZahl%10)
    whileZahl = whileZahl//10
    i += 1 
  return int(math.copysign(ergebnis, zahl))
  
print(whileLoved(zahl))


#ii) for

def forLoved(zahl):
  forZahl = abs(zahl)
  ergebnis = 0
  for i in range (0, int(math.log10(abs(zahl)))+1):
    if forZahl%10 != 0:
      ergebnis += (10**i) * (10 - forZahl%10)
    forZahl = forZahl // 10
  return int(math.copysign(ergebnis, zahl)) 
print(forLoved(zahl))


#iii) rekursion

def recursionLoved(zahl, ergebnis, counter):
  recZahl = abs(zahl)
  if int(recZahl) == 0:
    return int(ergebnis)
  else:
    if recZahl%10 != 0:
      return int(math.copysign(recursionLoved(recZahl//10, ergebnis + (10**counter) * (10 - recZahl%10), counter+1), zahl))
    else:
      return int(math.copysign(recursionLoved(recZahl//10, ergebnis + 0 , counter+1), zahl))
    

print(recursionLoved(zahl, 0, 0))