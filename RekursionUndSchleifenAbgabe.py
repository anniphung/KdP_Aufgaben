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
Voraussetzung: Eingabe ist positive Integer
Effekt: - 
Ergebnis: Zahl mit den verliebten Ziffern der Eingabe (Vorzeichen wird nicht erhalten)
'''

#For Schleife
def lovedDigits_F(n):
    
    erg = 0
    place = 1
    for i in range(n):
        lastDigit = n % 10
        if lastDigit == 0:
            lovedDigit = 0
        else:
            lovedDigit = 10 - lastDigit
        erg = erg + (lovedDigit * place)
        place *= 10
        n // 10
        if n == 0:
            break
    return erg
print(lovedDigits_F(-123))

#While: 
def lovedDigits_W(n):
    erg = 0
    place = 1

    while n > 0:
        lastDigit = n % 10
        if lastDigit == 0:
            lovedDigit = 0
        else:
            lovedDigit = 10 - lastDigit
        erg = erg + (lovedDigit * place)
        place *= 10
        n //= 10
    return erg

print(lovedDigits_W(-123))

#Rekursion:
def lovedDigits_R(n):
    if n == 0:
        return 0
    else:
        lastDigit = n % 10
        if lastDigit == 0:
            lovedDigit = 0
        else:
            lovedDigit = 10 - lastDigit

        remaining_n = n // 10
    return lovedDigit + (lovedDigits_R(remaining_n)* 10)

print(lovedDigits_R(123))
