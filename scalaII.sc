//a)
/*
Vor: Eingabe ist eine Liste bestehend aus Integers
Eff: - 
Ergebnis: List in der jeder Eintrag der ursprünglichen Liste verdoppelt wurde
*/

def doubleListRek(list: List[Int]): List[Int] = 
  list match 
  case List() => List()
  case _ => 2 * list.head :: doubleListRek(list.tail)

//Test a) Rek)
println("\nTest doubleListRek \n")
println(doubleListRek(List(1,2,3,4)))
println(doubleListRek(List(-1,-2,-3,-4)))
println(doubleListRek(List(0)))
println(doubleListRek(List()))

def doubleListERek(list: List[Int]): List[Int] = 
  def helper(l: List[Int], acc:List[Int]): List[Int] = 
    l match 
    case Nil => acc
    case x :: xs => helper(xs, acc :+ 2*x)
  helper(list, Nil)

//Test a) ERek)
println("\nTest doubleListERek \n")
println(doubleListERek(List(1,2,3,4)))
println(doubleListERek(List(-1,-2,-3,-4)))
println(doubleListERek(List(0)))
println(doubleListERek(List()))


/*doubleListERek ist endrekursiv, da die letzte ausgeführte Operation immer help(xs, acc:+2) ist also der rekursive Aufruf (außer im Rekursionsanker).
Zudem wird, wie es für die Endrekursion typisch ist, eine Hilfsfunktion mit Akkumulator benutzt.*/

//b)
/*
Vor: Liste aus Integern und ganze Zahl werden übergeben. 
Eff: - 
Ergebnis: Boolean, der angibt, ob die Zahl in der Liste enthalten ist.
*/
def linSearch(list: List[Int], number: Int): Boolean = 
  if list.isEmpty then
    false
  else
    list.head match
      case n if n == number => true
      case _ => linSearch(list.tail, number)

//Tests b)
println("\nTest linSearch \n")
println(linSearch(List(1,6,3,2),3))
println(linSearch(List(1,6,3,2),-5))
println(linSearch(List(),0))

//c)
/*
Vor: Eine Liste bestehend aus Integern und eine ganze Zahl werden übergeben.
Eff: - 
Ergebnis: Ein Tupel bestehend aus entweder (x,y) mit x + y = k oder (-1, k) falls es keine x, y mit x + y = k gibt
*/
def twoSumList(list: List[Int], number: Int): (Int, Int) = 
  if list.isEmpty then
    (-1, number)
  else
    if linSearch(list.tail, number - list.head) then 
      (list.head, number - list.head)
    else
      twoSumList(list.tail, number)

//Tests c)
println("\nTest twoSumList \n")
println(twoSumList(List(1,6,3,2),3))
println(twoSumList(List(1,6,3,2),-5))
