'Spezifikation:'
'Pre: Variable zahl ist größer 0'
'Effekt: - '
'Ergebnis: Trollifizierte Zahl'


def countAsTroll(zahl):
  if zahl == 0:
    return ''
  elif zahl - 16 >= 0:
    return 'LOTS-' + countAsTroll(zahl-16)
  elif zahl - 4 >= 0:
    return 'Many-' + countAsTroll(zahl-4)
  elif zahl == 3:
    return 'three'
  elif zahl == 2:
    return 'two'
  else:
    return 'one'

  
print(countAsTroll(6))

def trollToInt(trollzahl: str) -> int:
  words = trollzahl.split('-')
  ganzeZahl = 0
  for x in words:
    if x == 'LOTS':
      ganzeZahl += 16
    elif x == 'Many':
      ganzeZahl += 4
    elif x == 'three':
      ganzeZahl += 3
    elif x == 'two':
      ganzeZahl += 2
    elif x == "one":
      ganzeZahl += 1
  return ganzeZahl

print(trollToInt('Many-one'))

