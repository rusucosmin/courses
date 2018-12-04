// An example worksheet, run it using the button above!

1 + 1

def foo(x: Int): Int  = x * 2

foo(21)


final case class Vertex(id: Int, neighbors: List[Int])
final case class Graph(vertices: List[Vertex])

abstract class Formula
final case class Var(name: String) extends Formula
final case class Not(p: Formula) extends Formula
final case class And(p: Formula, q: Formula) extends Formula
final case class Or(p: Formula, q: Formula) extends Formula
final case class Implies(p: Formula, q: Formula) extends Formula

def graphColoring(graph: Graph): Formula = graph match {
  case Graph(vertices) => Var("1R")
}

def pairAverageAux(xs: Stream[Double], last: Double): Stream[Double] = xs match {
  case Stream.Empty => Stream.empty
  case x #:: t => ((x + last) / 2) #:: pairAverageAux(t, x)
}





def pairAverages(data: Stream[Double]): Stream[Double] = data match {
  case Stream.Empty => Stream.empty
  case x #:: xs => pairAverageAux(xs, x)
}





pairAverages(1.0 #:: 1.0 #:: 4.0 #:: 5.0 #:: 7.0 #:: 0.0 #:: Stream.empty).toList

def windowAverageAux(windowSize: Double, data: Stream[Double], soFar: List[Double], k: Int): Stream[Double] = {
  if (k < windowSize) {
    data match {
      case Stream.Empty => Stream.Empty
      case x #:: xs => windowAverageAux(windowSize, xs, soFar ++ List(x), k + 1)
    }
  } else {
    data match {
      case Stream.Empty => (soFar.foldLeft(0.0)(_ + _) / windowSize) #:: Stream.Empty
      case x #:: xs => (soFar.foldLeft(0.0)(_ + _) / windowSize) #:: windowAverageAux(windowSize, xs, soFar.tail ++ List(x), k + 1)
    }
  }
}

















def windowAverage(windowSize: Double, data: Stream[Double]): Stream[Double] =
  windowAverageAux(windowSize, data, Nil, 0)

windowAverage(2, 1.0 #:: 1.0 #:: 4.0 #:: 5.0 #:: 7.0 #:: Stream.empty).toList
windowAverage(3, 1.0 #:: 2.0 #:: 5.0 #:: 8.0 #:: 15.0 #:: Stream.empty).toList

def rollingAverageAux(data: Stream[Double], k: Int, acc: Double): Stream[Double] = data match {
  case Stream.Empty => Stream.Empty
  case x #:: xs => ((acc + x) / (k + 1)) #:: rollingAverageAux(xs, k + 1, acc + x)
}






def rollingAverage(data: Stream[Double]): Stream[Double] = data match {
  case Stream.Empty => Stream.Empty
  case x #:: xs => x #:: rollingAverageAux(xs, 1, x)
}








rollingAverage(1.0 #:: 2.0 #:: 3.0 #:: 4.0 #:: 5.0 #:: Stream.empty).toList



def substitute(term: Any, symbol: Symbol, replaceBy: Any): Any = term match {
  case x: Symbol => if (x == symbol) replaceBy else x
  case x: List[Any] => x map (substitute(_, symbol, replaceBy))
  case x => x
}
substitute(List('+, 'a, List('+, 2, 'a)), 'a, 1)


val square: Stream[Int] = Stream.from(1).map((x) => x * x)

def zeroOneStream(x: Stream[String]): Stream[String] = {
  val incr: Stream[String] = (x map (_ + "0")) #::: (x map (_ + "1"))
  incr #::: zeroOneStream(incr)
}
def zeroOne(): Stream[String] = {
  zeroOneStream(Stream(""))
}
val codes = zeroOneStream(Stream(""))

val palCodes: Stream[String] = codes.filter((x) => x.reverse == x)
val palCodesv2: Stream[String] = codes.foldLeft[Stream[String]](Stream.Empty)((x, y) => if (y.reverse == y) x #::: Stream(y) else x)


palCodes.take(10).toList
palCodesv2.take(10).toList











