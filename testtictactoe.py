##--Erstellt ein leeres Spielfeld / Skript vom Aufgabenblatt--##
SpielFeld = [3*[None] for i in range(3)]
spieler = "X"

##-Signatur: Eraselines(amount)
##--Vorraussetzung: Eingabe ist ein Int
##--Effekt: Bewegt den Cursor [amount]mal nach oben im Output
##--Ergebnis: löscht somit effektiv eine Zeile
## ---Testfall: Eraselines(1) -> Eine Zeile wird gelöscht
def EraseLines(amount):
    i= amount
    while i > 0:
        print("\x1B[F\x1B[2K", end="")
        i -= 1

##-Signatur: buildline(reihe)
##--Vorraussetzung: Eingabe ist eine Liste
##--Effekt: Gibt die Liste mit zwischen Linien aus
##--Ergebnis: Dekorativer Listen Print
## ---Testfall: buildline((X,X,X)) -> |X|X|X|
def buildline(reihe):
    for i in reihe:
        print("", end="|")
        if not i is None:
            print(i, end= "")
        else:
            print(" ", end= "")
    print("", end="|")
    print("\n")

##-Signatur: printBoard(SpielFeld)
##--Vorraussetzung: Eingabe ist eine Liste von Listen
##--Effekt: ruft buildline(i) für jede Liste in der Liste auf
##--Ergebnis: Dekorativer Print von vielen Listen in einer Liste
## ---Testfall: printBoard(SpielFeld((X,X,X),(X,X,X),(X,X,X))) -> |X|X|X| (neue Zeile) |X|X|X| (neue Zeile) |X|X|X| (neue Zeile)
def printBoard(SpielFeld):
    for i in SpielFeld:
        buildline(i)

##-Signatur: CheckHorizontalWin(SpielFeld)
##--Vorraussetzung: Eingabe ist eine Liste von Listen
##--Effekt: Überprüft nach mindestens einer Gleichheit von Listeninnerein in einer Zeile
##--Ergebnis: Überprüft Horizontale Siegbedingungen für TicTacToe
## ---Testfall: CheckHorizontalWin(SpielFeld((X,X,X),(X,Y,Y),(Y,X,Y))) -> (True, X)
def CheckHorizontalWin(SpielFeld):
    for i in SpielFeld:
        if i[0] == i[1] and i[0] == i[2] and not i[0] is None:
            return (True, str(i[0]))

    return(False, None)

##-Signatur: CheckDiagonalWin(SpielFeld)
##--Vorraussetzung: Eingabe ist eine Liste von Listen
##--Effekt: Überprüft nach mindestens einer Gleichheit von Listeninnerein in Diagonalen Obenlinks zu Untenrechts und Obenrechts zu Untenlinks Positionen
##--Ergebnis: Überprüft Diagonale Siegbedingungen für TicTacToe
## ---Testfall: CheckHorizontalWin(SpielFeld((X,X,X),(X,Y,Y),(Y,X,Y))) -> (False, None)
def CheckDiagonalWin(SpielFeld):
    
    j = SpielFeld[0]
    k = SpielFeld[1]
    l = SpielFeld[2]

    if not j[0] is None and j[0] == k[1] and j[0] == l[2] :
        return (True, str(j[0]))
    if not j[2] is None and j[2] == k[1] and j[2] == l[0]:
        return (True, str(j[2]))
    
    return(False, None)

##-Signatur: CheckVerticalWin(SpielFeld)
##--Vorraussetzung: Eingabe ist eine Liste von Listen
##--Effekt: Überprüft nach mindestens einer Gleichheit von Listeninnerein in einer spalte
##--Ergebnis: Überprüft Vertikale Siegbedingungen für TicTacToe
## ---Testfall: CheckHorizontalWin(SpielFeld((X,X,X),(X,Y,Y),(Y,X,Y))) -> (False, None)
def CheckVerticalWin(SpielFeld):
    
    j = SpielFeld[0]
    k = SpielFeld[1]
    l = SpielFeld[2]

    if not j[0] is None and j[0] == k[0] and j[0] == l[0] :
        return (True, str(j[0]))
    if not j[1] is None and j[1] == k[1] and j[1] == l[1]:
        return (True, str(j[1]))
    if not j[2] is None and j[2] == k[2] and j[2] == l[2]:
        return (True, str(j[2]))
    
    return(False, None)

##-Signatur: CheckAllWin(SpielFeld)
##--Vorraussetzung: Eingabe ist eine Liste von Listen
##--Effekt: Wertet Ergebnisse von allen anderen Check...Win(SpielFeld) Funktionen aus
##--Ergebnis: Überprüft alle Siegbedingungen für TicTacToe
## ---Testfall: CheckHorizontalWin(SpielFeld((X,X,X),(X,Y,Y),(Y,X,Y))) -> (True, X)
def CheckAllWin(SpielFeld):
    HorizontalWin = CheckHorizontalWin(SpielFeld)
    VerticalWin = CheckVerticalWin(SpielFeld)
    DiagonalWin = CheckDiagonalWin(SpielFeld)
    AllWin = (HorizontalWin, VerticalWin, DiagonalWin)

    if bool(HorizontalWin[0]) == True or bool(VerticalWin[0]) == True or bool(DiagonalWin[0]) == True:
        for i in AllWin:
            if not i[1] is None:
                return(True, i[1])
    
    return(False, None)

##-Signatur: CheckField(Spielfeld, ZielZeile, ZielSpalte)
##--Vorraussetzung: Eingabe1 ist eine Liste von Listen, Eingabe2 und Eingabe3 sind Int
##--Effekt: Überprüft ob die Position die der Spieler angibt bereits besetzt ist
##--Ergebnis: Validierungsschritt der Spielerposition
## ---Testfall: SpielFeld((None,O,X),(X,O,None),(None,X,None)), Zielzeile = 2, Zielspalte = 2 -> False
def CheckField(SpielFeld, ZielZeile, ZielSpalte):
        n = 0
        for i in SpielFeld:
            if n == (int(ZielZeile) - 1) and not i[int(ZielSpalte) - 1] is None:
                return(False)
            n += 1
        return(True)
  
##-Signatur: PlaceSign(Spieler, SpielFeld)
##--Vorraussetzung: Eingabe1 ist ein String und Eingabe2 ist eine Liste von Listen
##--Effekt: Erbitter Positions Input, Validiert den Input und Ändert an der Eingegebenen Position den Wert zu Eingabe1 
##--Ergebnis: Platziert X/O an der von Spieler gewählten Position
## ---Testfall: PlaceSign("X", SpielFeld((None,O,X),(X,O,None),(None,X,None))), ZielZeile = 3, ZielSpalte = 3 -> SpielFeld((None,O,X),(X,O,None),(None,X,X))
def PlaceSign(Spieler, SpielFeld):
    n = 0
    ZielZeile = input(Spieler + ", Trage die Zeile für dein nächsten Spielschritt ein.\n\n ->     "  )
    EraseLines(3)
    ZielSpalte = input(Spieler + ", Trage die Spalte für dein nächsten Spielschritt ein.\n\n ->     "  )
    EraseLines(3)

    while ZielZeile.isdigit() == False or ZielSpalte.isdigit() == False or CheckField(SpielFeld, ZielZeile, ZielSpalte) == False:
        print("Der von Ihnen gewählte Input entspricht nicht den Vorraussetzungen.")
        ZielZeile = input(Spieler + ", Trage die Zeile für dein nächsten Spielschritt ein.\n\n ->     ")
        EraseLines(3)
        ZielSpalte = input(Spieler + ", Trage die Spalte für dein nächsten Spielschritt ein.\n\n ->     "  )       
        EraseLines(4)
    
    for i in SpielFeld:
        if n == (int(ZielZeile) - 1):
            i[int(ZielSpalte) - 1] = Spieler
        n += 1
    
    EraseLines(6)
    printBoard(SpielFeld)

##-Signatur: ticTacToe()
##--Vorraussetzung: /
##--Effekt: Ändert nach jeden PlaceSign() den Spieler und nutzt CheckAllWin(SpielFeld) um Spielstand zu überprüfen
##--Ergebnis: Erlaubt zwei Spieler TicTacToe zu spielen
## ---Testfall: ticTacToe(), CheckAllWin((True, "X")) -> "You Won, X"
def ticTacToe():
    global spieler
    gamewon = False
    while gamewon == False:
        if spieler == "X":
            spieler = "O"
        elif spieler == "O":
            spieler = "X"

        
        checktupel = CheckAllWin(SpielFeld)
        gamewon = bool(checktupel[0])

        if gamewon == False:
            PlaceSign(spieler, SpielFeld)
        else:
            print("Du hast gewonnen", checktupel[1])

printBoard(SpielFeld)
ticTacToe()




