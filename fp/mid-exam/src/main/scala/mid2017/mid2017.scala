package mid2017

object Mid2017 {
  def insert(elem: Int, list: List[Int]): List[Int] = list match {
    case Nil => List(elem)
    case x :: xs =>
      if (elem <= x) elem :: x :: xs
      else x :: insert(elem, xs)
  }

  def findKLargestElements(k: Int)(list: List[Int]): List[Int] = {
    def _insert(topK: List[Int], el: Int): List[Int] = {
      val inserted = insert(el, topK)
      if (inserted.size > k)
        inserted.tail
      else
        inserted
    }
    list.foldLeft(List[Int]())(_insert)
  }
  def computeFlips(square: Square): List[Square] = {
    /*
    List(-1, 0, 1).flatMap { i =>
      List(-1, 0, 1).filter { j =>
        i != 0 || j != 0
      }.flatMap { j =>
        computeFlipsInDirection(square, i, j)
      }
    }
    */
    for {
      i <- List(-1, 0, 1)
      j <- List(-1, 0, 1)
      if i != 0 || j != 0
      x <- computeFlipsInDirection(square, i, j)
    } yield {
      x
    }
  }
  def computeFlipsInDirection(square: Square, dirX: Int, dirY: Int): List[Square] = {
    Nil
  }

}
final case class Square(x: Int, y: Int);

class Function[-U, +V]
class PureFunction[-U, +V] extends Function[U, V]

class Chan[-P, +R]
class FixedChan[P, +R] extends Chan[P, R]

class B
class Y
class A extends B
class X extends Y

