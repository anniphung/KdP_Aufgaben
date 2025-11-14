import math

#a)

'''
Signatur: multiplyAllBy_X(xs:list[int], n: int) -> list[int]
Voraussetzung: Liste xs besteht aus ganzen Zahlen und n ist eine ganze Zahl ungleich 0
Effekt: -
Ergebnis: Ausgabe ist eine Liste in der die Elemente der ersten Liste mit n multipliziert stehen
'''

#For Schleife
def multiplyAllBy_F(xs,n):
    erg = []
    for elem in xs:
        produkt = elem * n
        erg.append(produkt)
    return erg
print(multiplyAllBy_F([1,2,3],4))

#While Schleife
def multiplyAllBy_W(xs,n):
    erg = []
    i = 0
    while i < len(xs):
        elem = xs[i]
        produkt = elem * n
        erg.append(produkt)
        i += 1
    return erg
print(multiplyAllBy_W([1,2,3],4))

#Rekursion
def multiplyAllBy_R(xs,n):
    if len(xs) == 0:
        return[]

    headerg = xs[0]*n
    tailerg = multiplyAllBy_R(xs[1:],n)

    return [headerg] + tailerg

print(multiplyAllBy_R([1,2,3],4))

#b)
'''
lovedDigits_X(n: int)-> int
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