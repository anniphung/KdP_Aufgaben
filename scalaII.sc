//a)
/*
Vor: Eingabe ist eine Liste bestehend aus Integers
Eff: - 
Ergebnis: List in der jeder Eintrag der ursprünglichen Liste verdoppelt wurde
*/

def doubleListRek(list: List[Int]): List[Int] = 
  list match 
    case List() => List()
    case x::xs => 2 * x :: doubleListRek(xs)

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
  list match
    case Nil => false
    case x::xs if x == number => true
    case x::xs => linSearch(xs, number)

//Tests b)
println("\nTest linSearch \n")
println(linSearch(List(1,6,3,2),3))
println(linSearch(List(1,6,3,2),-5))
println(linSearch(List(),1))
println(linSearch(List(0),0))

//c)
/*
Vor: Eine Liste bestehend aus Integern und eine ganze Zahl werden übergeben.
Eff: - 
Ergebnis: Ein Tupel bestehend aus entweder (x,y) mit x + y = k oder (-1, k) falls es keine x, y mit x + y = k gibt
*/
def twoSumList(list: List[Int], number: Int): (Int, Int) = 
  list match
    case Nil => (-1, number)
    case x::xs if linSearch(xs, number - x) => (x, number - x)
    case x::xs => twoSumList(xs, number)

//Tests c)
println("\nTest twoSumList \n")
println(twoSumList(List(1,6,3,2),3))
println(twoSumList(List(1,6,3,2),-5))
println(twoSumList(List(),1))
println(twoSumList(List(0),0))
println(twoSumList(List(0,0),0))
