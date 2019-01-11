

def flatMap[T](list: List[T], f: T => List[T]): List[T] = {
  def reverse(list: List[T], acc: List[T]): List[T] = list match {
    case Nil => acc
    case x :: xs => reverse(xs, x :: acc)
  }
  def flatten(list: List[List[T]], acc: List[T]): List[T] = list match {
    case Nil => acc
    case x :: xs => x match {
      case Nil => flatten(xs, acc)
      case y :: ys => flatten(ys :: xs, y :: acc)
    }
  }
  def flatMapAux(list: List[T], acc: List[List[T]]): List[T] = list match {
    case Nil => flatten(acc, Nil)
    case x :: xs => flatMapAux(xs, reverse(f(x), Nil) :: acc)
  }
  flatMapAux(list, Nil)
}

val f = x: Int => List(x, x + 1)

assert(flatMap(List(1, 2, 3), f) == List(1, 2, 2, 3, 3, 4))

val x: Stream[Stream[String]] = Stream(Stream("a1", "a2", "a3", "a4"), Stream("b1", "b2", "b3", "b4"),
  Stream("c1", "c2", "c3", "c4"))

def transpose(src: Stream[Stream[String]]): Stream[Stream[String]] = {
  def _transpose(streams: Stream[Stream[String]], i: Int): Stream[Stream[String]] = streams match {
    case Stream.Empty => Stream.Empty
    case _ #:: sr => src.map(s => s(i)) #:: _transpose(sr, i + 1)
  }
  _transpose(src, 0)
}

print(transpose(x)(0).toList)
print(transpose(x)(1).toList)
print(transpose(x)(2).toList)