spieler = {'x': input('Spieler 1, bitte gebe deinen Namen ein: '),
           'o': input('Spieler 2, bitte gebe deinen Namen ein: ')}

#a
print(f"{spieler['x']} du spielst x, und {spieler['o']} du spielst o. Bitte gebt die Position auf die ihr setzen wollt mit einer Koordinate zwischen (0,0) und (2,2) an.")

'''
Pre: Die Postition ist ein tupel von Ints und das Spielfeld eine Liste von Listen
Eff: Falls notwendig werden Fehlermeldungen gedruckt
Res: Boolean der angibt, ob die Position gültig ist
'''
def positionCheck(position: tuple, spielfeld: list) -> bool:
  if (position[0]==None or position[1]==None):
    return False
  elif not (0<=position[0]<=2 and 0<= position[1]<= 2):
    print('Deine Position muss zwischen (0,0) und (2,2) liegen')
    return False
  elif not (spielfeld[position[0]][position[1]]) == None:
    print('Diese Position ist bereits besetzt. Bitte wähle eine andere Position.')
    return False
  else:
    return True 


'''
Pre: Das Zeichen des momentanen Spielers ist im Wörterbuch spieler (mit dem zugehörigen Namen des Spielers), außerdem ist das Spielfeld aktuell und eine Liste von Listen
Eff: Im Falle eines Fehlers (Eingabe nicht als Integer interpretierbar) wird die Fehlermeldung ausgegeben 
Res: Das aktualisierte Spielfeld (mit neu gesetztem Zeichen des Spielers) wird zurückgegeben
'''
def placeSign(spielerSign: str, spielfeld: list) -> list:
  position = (None, None)
  print(f'{spieler[spielerSign]} auf welche Position im Spielfeld möchtest du {spielerSign} setzen?')
  while not positionCheck(position,spielfeld):                                                                #Spieler wird wiederholt nach Eingabe der Koordinaten gefragt, bis sie gültig sind
    try:
      zeile = int(input('In welche Zeile soll dein Zeichen gesetzt werden?: '))
      spalte = int(input('In welche Spalte soll dein Zeichen gesetzt werden?: '))
      position = (zeile, spalte)
    except:
      print('Deine Eingabe lässt sich nicht als Integer interpretieren. Bitte gebe nur ganze Zahlen ein.')
      continue
  aktuellSpielfeld = spielfeld
  aktuellSpielfeld[position[0]][position[1]] = spielerSign
  return aktuellSpielfeld

#b
'''
Pre: Liste existiert und enthält ausschließlich Strings oder NoneType 
Eff: - 
Res: String mit Inhalte der Liste durch | getrennt
'''
def buildLine(reihe: list) -> str:
  line = ''
  for i in range(0, len(reihe)):                           #Zum Iterieren über die Reihe im Spielfeld
    if reihe[i] == None:                            
      value = ' '                                          #Damit None als Leerzeichen ausgegeben wird, neue Variable value habe ich angelegt, damit das Spielfeld selbst nicht überschrieben wird
    else:
      value = reihe[i]                                    
    if i < len(reihe)-1:
      value = value + '|'                                  #Striche bei aneinandergenzenden Zellen des Spielfelds, damit es leichter lesbar ist
    line = line + value                                    #Strings werden Konkateniert
  return line
  
#c
'''
Pre: Spielfeld ist eine Liste von Listen von Strings und Nonetype
Eff: Druckt das Spielfeld 
Res: - 
'''
def printBoard(spielfeld:list)-> None:
  printSpielfeld = spielfeld
  for reihe in printSpielfeld:
    print(buildLine(reihe))

#d
'''
Pre: Spielfeld ist eine Liste von Listen
Eff: - 
Res: Tupel je nachdem ob gewonnen wurde (True, Spielername) oder (False, None)
'''
def checkRows(spielfeld:list)-> tuple:
  for row in spielfeld:
    if row[0] == row[1] == row[2] != None:                 #sind alle Einträge gleich in Reihe?
      return (True, spieler[row[0]])
  return (False, None)

'''
Pre: Spielfeld ist eine Liste von Listen und ist 'quadratisch' Anzahl Listen = Anzahl einträge in den Listen 
Eff: - 
Res: Tupel je nachdem ob gewonnen wurde (True, Spielername) oder (False, None)
'''
def checkColumns(spielfeld:list)-> tuple:
  columns = []
  for i in range(0, len(spielfeld)):                       #for Schleifen über Anzahl der Spalten die es bei quadratischem Spielfeld gibt 
    columns.append([])
    for j in range(0, len(spielfeld)):                     #Variable für Spalten wird erstellt
      columns[i].append(spielfeld[j][i])
  for column in columns:
    if column[0] == column[1] == column[2] != None:       #alle Einträge in Spalte gleich?
      return (True, spieler[column[0]])
  return (False, None)

'''
Pre: Spielfeld ist eine Liste von Listen
Eff: - 
Res: Tupel je nachdem ob gewonnen wurde (True, Spielername) oder (False, None)
'''
def checkDiagonals(spielfeld:list)-> tuple:
  diagonals = [[],[]]
  for i in range(0,len(spielfeld)):
    diagonals[0].append(spielfeld[i][i])                                #Diagonale von links nach rechts
  for j in range(0, len(spielfeld)):
    diagonals[1].append(spielfeld[j][len(spielfeld)-1-j])               #Diagobale von rechts nach links
  for diagonal in diagonals:
    if diagonal[0] == diagonal[1] == diagonal[2] != None:               #hat eine Diagonale alle Einträge gleich?
      return (True, spieler[diagonal[0]])
  return (False, None)

'''
Pre: Spielfeld ist Liste von Listen  
Eff: -
Res: Tupel je nachdem ob gewonnen wurde (True, Spielername) oder (False, None) 
'''
def checkWin(spielfeld:list)-> tuple:
  if checkRows(spielfeld)[0]:
    return checkRows(spielfeld)
  elif checkColumns(spielfeld)[0]:
    return checkColumns(spielfeld)
  elif checkDiagonals(spielfeld)[0]:
    return checkDiagonals(spielfeld)
  else:                                               #gibt es einen Gewinn oder nicht Fallunterscheidung
    return (False, None)

#e)
'''
Pre: -
Eff: Lässt 2 Spieler TicTacToe spielen
Res: - 
'''
def ticTacToe()-> None:
  spielfeld = [3*[None] for i in range(3)]
  currentPlayer = 'x'
  printBoard(spielfeld)
  while checkWin(spielfeld)[0] == False:                              #Während nicht gewonnen ist
    if None in [value for row in spielfeld for value in row]:         #Während es noch Elemente == None gibt (Spielfeld noch nicht ausgefüllt)
      spielfeld = placeSign(currentPlayer, spielfeld)
      printBoard(spielfeld)
      currentPlayer = 'o' if currentPlayer == 'x' else 'x'            #Toggle Spieler
    else:
      print('Unentschieden')
      return
  print(f'{checkWin(spielfeld)[1]} hat gewonnen!')  
  return

ticTacToe()