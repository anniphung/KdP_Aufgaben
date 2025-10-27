#Blatt 2 Aufgabe 1: Galgenmännchen 

fehlerBild = [   r"""
              





  wwwww
w ww w www w wwww w w""", 
                        r""" 
    
    | 
    |               
    |     
    |       
    |      
    |   
  wwwww
w ww w www w wwww w w""", 
                        r""" 
    __________
    | 
    |               
    |     
    |      
    |      
    |   
  wwwww
w ww w www w wwww w w""", 
                        r""" 
    __________
    | /     
    |               
    |     
    |       
    |      
    |   
  wwwww
w ww w www w wwww w w""", 
                        r""" 
    __________
    | /      |
    |      (@ @)       
    |     
    |       
    |      
    |   
  wwwww
w ww w www w wwww w w""", 
                        r""" 
    __________
    | /      |
    |      (@ @)           
    |        |
    |        |
    |      
    |   
  wwwww
w ww w www w wwww w w""", 
                        r""" 
    __________
    | /      |
    |      (@ @)           
    |      \ | 
    |        | 
    |      
    |   
  wwwww
w ww w www w wwww w w""", 
                        r""" 
    __________
    | /      |
    |      (@ @)           
    |      \ | /
    |        | 
    |      
    |   
  wwwww
w ww w www w wwww w w""", 
                        r""" 
    __________
    | /      |
    |      (@ @)           
    |      / | \
    |        | 
    |       /
    |   
  wwwww
w ww w www w wwww w w""", 
                        r""" 
    __________
    | /      |
    |      (x x)           
    |      / | \
    |        | 
    |       / \ 
    |   
  wwwww
w ww w www w wwww w w"""]


nameSpieler1 = input('Bitte gebe deinen Namen ein Spieler 1: ')
nameSpieler2 = input('Bitte gebe deinen Namen ein Spieler 2: ')

wort = input(nameSpieler1 + ', bitte denke dir ein Wort aus, das ' + nameSpieler2 + ' erraten soll und gebe es ein: ')

while not (wort.isalpha()):
  wort = input('Bitte gebe ein Wort ein, das ausschließlich aus Buchstaben besteht: ')

wort= wort.lower()

print( ' \n\n\n\n\n\n\n\n\n\n\n\n\n\n ' + nameSpieler2 + ', nun kannst du anfagen das Wort zu erraten. Die Eingabe ist nicht case sensitive, es spielt also keine Rolle, ob der Buchstabe groß oder klein geschrieben wird. Du hast insgesamt 10 Versuche.')

wortProgress = ['_']*len(wort)

print(*wortProgress)

fehlerCounter = 0

while ('_' in wortProgress) and (fehlerCounter < 10):
  guess = input('Rate einen Buchstaben: ')
  while not (guess.isalpha and len(guess) == 1):
    guess = input('Bitte gebe einen Buchstaben ein: ')
  guess = guess.lower()
  if guess in wort:
    print('\n Das war ein richtiger Buchstabe. \n')
    for i in range(0, len(wort)):
      if wort[i] == guess:
        wortProgress[i] = guess
        print(*wortProgress, '\n')
  else:
    fehlerCounter += 1
    print('\n Der Buchstabe ist nicht im Wort. \n ', *wortProgress)
    print(fehlerBild[fehlerCounter-1], '\n')
  
if '_' in wortProgress:
  print('Du hast verloren')
else:
  print('Herzlichen Glückwunsch! Du hast gewonnen! :D')