def isSorted(list: List[Int]): Boolean = 
  list match
    case Nil => true       //Rekursionsanker
    case x::Nil => true    //Rekursionsanker
    case x::y::xs if x <= y => isSorted(y::xs)  //Rekursschritt
    case x::y::xs => false  //Rekursionsanker

println(isSorted(List(1,2,3,4,5)))
    