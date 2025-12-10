val date = (12, 6, 2006)

def julianDate(date:(Int,Int,Int)):(Int,Int,Int)=
  val (d,m,j) = date
  if (m == 1 || m == 2) then
    (d,m+10,j-1)
  else
    (d,m-2,j)

println(julianDate(date))

//a)
/*
Vor: Datum wird als gregorianisches Kalenderdatum angegeben im Format dd.mm.yyyy oder d.m.yyyy (beziehungsweise eine Kombination aber das Jahr muss komplett ausgeschrieben werden).
Eff: - 
Ergebnis: Ganze Zahl zwischen 1 und 7, die den Wochentag angibt. 
*/
def wDay(jDate: (Int, Int, Int)): Int =
  val day = jDate(0)
  val month = jDate(1)
  val century = jDate(2)/100
  val year = jDate(2) - century*100
  ((day + math.floor(2.6 * month - 0.2) + year + math.floor(year/4) + math.floor(century/4) - 2 * century).toInt % 7 + 7) % 7

println(wDay(julianDate(date)))

//b)
/*
Vor: Eingabe ist eine Zahl zwischen 1 und 7.
Eff: - 
Ergebnis: String der den zugehörigen Wochentag angibt.
*/
def intToDay(wDay: Int): String = 
  wDay match
    case 1 => "Monday"
    case 2 => "Tuesday"
    case 3 => "Wednesday"
    case 4 => "Thursday"
    case 5 => "Friday"
    case 6 => "Saturday"
    case 7 => "Sunday"
    case x => throw Exception( x + "Is not a valid weekday number.")

println(intToDay(wDay(julianDate(date))))

//c)
/*
Vor: Datum wird als gregorianisches Kalenderdatum angegeben im Format dd.mm.yyyy oder d.m.yyyy (beziehungsweise eine Kombination aber das Jahr muss komplett ausgeschrieben werden).
Eff: - 
Ergebnis: String des Wochentags des Datums.
*/
def dateToDay(date: (Int,Int,Int)): String = 
  intToDay(wDay(julianDate(date)))