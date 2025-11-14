# Definition 1
def askFor1(a:str) -> str:
  global z
  global y
  if a == "Passierschein A39":
    z = "Passierschein A38"
    y = "Präfekt"
  elif a == "Rundschreiben B56":
    x = "Niemand"
    z = "alles"
  else:
    z = "dem hellbraunen Formular"
    print("Sie gehen zu Schalter 56.")

# Definition 2
def askFor2(a:str) -> str:
  global x
  global y
  if a == "Passierschein A39":
    z = "Passierschein A38"
    y = "Präfekt"
  elif a == "Rundschreiben B56":
    x = "Niemand"
    z = "alles"
  else:
    z = "dem hellbraunen Formular"
    print("Sie gehen zu Schalter 56.")

def getWhatVarWants(x:str) -> str:
  z = "Rundschreiben B56"
  if x == "dem hellbraunen Formular":
    z = "Passierschein A39"
    print("Sie suchen ",z)
  askFor1(z)

x = "Asterix"
y = "Obelix"
z = "Formular A38"
print(x," & ",y,"suchen ",z,".")
askFor1(z)
print("Sie fragen nach ",z,".")
getWhatVarWants(z)
print(x," erhält ",z,".")
print(y," verliert und wird verrückt.")


'''Def1
Asterix  &  Obelix suchen  Formular A38 .
Sie gehen zu Schalter 56.
Sie fragen nach  dem hellbraunen Formular .
Sie suchen  Passierschein A39
Asterix  erhält  Passierschein A38 .
Präfekt  verliert und wird verrückt.
'''

''' Def2
Asterix  &  Obelix suchen  Formular A38 .
Sie gehen zu Schalter 56.
Sie fragen nach  Formular A38 .
Niemand  erhält  Formular A38 .
Obelix  verliert und wird verrückt.
'''
