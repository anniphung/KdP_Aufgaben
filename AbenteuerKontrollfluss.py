name = input('Wie heißt du? ')
print("Hi " + name + "! " + "Willkommen im Abenteuer. Du wirst vor eine Reihe an Entscheidungen gestellt werden, bei denen du aus vier möglichen Vorgehensweisen wählen kannst. Bestätige die Antwort die du wählst einfach mit der zugehörigen Zahl." + "\n" +  "Nach einer langen Wanderung stehst auf einem kleinen Plateu in den Bergen. Hinter dir liegt eine saftig grüne Wiese, vor dir der Einang zu einer dunklen Höhle in der ein Darche lebt. Dieser Drache ist jedoch nicht nur irgendein Drache, es ist der Drache, der seit Jahrhunderten in den umliegenden Dörfer in Angst und Schrecken verbreitet. Du bist nun auf der Mission die Angst und den Schrecken ein für alle Mal zu beenden. Alles was du bei dir hast sind etwas Proviant und dein Schwert")
ersteEntscheidung = input("Was tust du als erstes? \n 1 - Du rennst mit gezücktem Schwert schreiend in die Höhle. \n 2 - Du schleichst ganz leise in die Höhle und hast dein Schwert griffbereit. \n 3 - Mit dem bisschen Proviant, den du dabei hast baust du ein kleines Picknick auf und lädst den Drachen ein. \n 4 - Du hast viel zu viel Angst also läufst du ganz schnell wieder zurück ins Dorf. \n" + "Wie hast du dich entschieden? ")

while int(ersteEntscheidung) > 4: 
  ersteEntscheidung = input("Bitte gebe eine Zahl zwischen 1 und 4 ein. ")

if int(ersteEntscheidung) == 1: 
  print('GAME OVER! Du findest den Drachen in der Höhle vor. Er greift dich an und dein Schwert bringt als Gegenwehr überhaupt nichts. Der Drache freut sich darüber, dass sein Mittagessen diesmal direkt zu ihm gekommen ist.')
elif int(ersteEntscheidung) == 2:
  print('GAME OVER! Der Drache hasst Hausfriedensbruch und frisst dich.')
elif int(ersteEntscheidung) == 3:
  zweiteEntscheidung = input("Du hast ein kleines Picknick aufgebaut. Was tust du jetzt? \n 1 - Du rufst ganz laut Hallo. \n 2 - Du klopfst höflich an die Seite des Eingangs.")
  while int(zweiteEntscheidung) > 2:
    zweiteEntscheidung = input("Bitte entscheide dich für Option 1 oder 2")
  if int(zweiteEntscheidung) == 1:
    print('GAME OVER! Der Drache findet das unhöflich und frisst dich.')
  else:
    dritteEntscheidung = input("Der Drache kommt aus seiner Höhle und scheint sichtbar erfreut über das Essensangebot. Was tust du nun? \n 1 - Du bietest ihm ein Käsebrot an \n 2 - Du bietest ein Stück Fleisch an")
    while int(dritteEntscheidung) > 2:
      dritteEntscheidung = input("Bitte entscheide dich für Option 1 oder 2")
    if int(dritteEntscheidung) == 1:
      print("HAPPY END! Der Drache liebt Käse. Ab jetzt bringt ihr ihm immer Käse und er frisst nie wieder Menschen.")
    else: 
      print("GAME OVER! Der Drache frist das Fleisch und dich gleich mit.")
else: #int(ersteEntscheidung) == 4:
  print('GAME OVER! Du lebst - zunächst. Aber das nächste Mal als der Drache dein Dorf heimsucht bist du gerade unterwegs zu deiner Oma. Der Drache sieht dich und frisst dich auf.')




