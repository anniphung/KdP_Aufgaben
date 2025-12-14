//b)
/*
Vor: n ist nicht negativ, xs eine Liste
Eff: - 
Erg: Tupel aus zwei Listen, erste Liste hat die ersten n Elemente, zweite den Rest. 
*/

def mySplitAt[A](n: Int, xs: List[A]): (List[A], List[A]) = 
  (n, xs) match
    case (_, Nil) => (Nil, Nil)
    case (0, xs) => (Nil, xs)
    case (m, xs) => (xs.take(m), xs.drop(m))



//c)
/*
Vor: Zwei Listen als Eingabe xs, ys
Eff: - 
Erg: Eine Liste aus Tupeln, i-tes Tuple ist (xs(i), ys(i)). 
*/
def myZip[A, B](as: List[A], bs: List[B]): List[(A, B)] = 
  (as, bs) match
    case (a :: xs, b :: ys) => (a, b) :: myZip(xs, ys)
    case _ => Nil

@main def tests(): Unit = 
  println(myZip(List(1,2,3), List("a", "b","c", "d")))
  println(mySplitAt(2, List(1,2,3,4,5)))