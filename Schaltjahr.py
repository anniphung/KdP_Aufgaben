#Eingabe: Integer, Ausgabe: Bool
#Spezifikation: 
#               Voraussetzung: None bzw Jahr ≥ 0
#               Effekt: None
#               Ergebnis: True falls Schaltjahr und False falls kein Schaltjahr
#Funktion hier ergänzen

def schaltjahr(jahreszahl:int) -> bool:
  if jahreszahl % 4 == 0 and (jahreszahl % 100 != 0 or jahreszahl % 400 == 0) and jahreszahl >= 1582:
    return True
  #elif jahreszahl % 400 == 0:
    #return True
  else:
    return False

''' Test von Form: schaltjahr(jahreszahl) == erwartete Ausgabe bzw. not schaltjahr(jahreszahl) zulässig, wenn die Ausgabe vom Typ Bool 
sein sollte. Die Ergebnisse der Tests werden miteinander verknüpft. '''
def test():
  return(
  True
  and not schaltjahr(2025)
  and schaltjahr(2000)
  and schaltjahr(4000)
  and not schaltjahr(1582)
  and not schaltjahr(1200)
  )

#Test wir ausgeführt 
print(test())