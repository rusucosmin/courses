package example
import scala._

object Mid2015 extends Mid2015 with App {
}

trait Mid2015 {
  def differences(ls: List[Int]): List[Int] = {
    ls match {
      case Nil => Nil
      case x :: xs => {
        val diff = differences(xs)
        diff match {
          case Nil => List(x)
          case _ => 
            x :: (diff.head - x) :: diff.tail
        }
      }
    }
  }
  def rebuildList(ls: List[Int]): List[Int] = {
    ls match {
      case Nil => Nil
      case x :: xs => xs.scan(x)(_ + _)
    }
  }
}
