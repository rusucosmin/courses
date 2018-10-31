package mid2014
import scala._
import scala.annotation._

object Mid2014 extends Mid2014 with App {
}

trait Mid2014 {
  def merge[T](as: List[T], bs: List[T])(cmp: (T, T) => Boolean): List[T] = {
    (as, bs) match {
      case (_, Nil) => as
      case (Nil, _) => bs
      case (x :: xas, y :: ybs) => {
        if (cmp(x, y)) x :: merge(xas, bs)(cmp)
        else y :: merge(as, ybs)(cmp)
      }
    }
  }
  def merge2[T](as: List[T], bs: List[T])(cmp: (T, T) => Boolean): List[T] = {
    @tailrec
    def _merge(as: List[T], bs: List[T], acc: List[T]): List[T] = {
      (as, bs) match {
        case (_, Nil) => acc.reverse ++ as
        case (Nil, _) => acc.reverse ++ bs
        case (x :: xas, y :: ybs) => {
          if (cmp(x, y)) _merge(xas, bs, x :: acc)
          else _merge(as, ybs, y :: acc)
        }
      }
    }
    _merge(as, bs, List())
  }

  def iterate[T](x: T)(f: T => T): Stream[T] = {
    x #:: iterate(f(x))(f)
  }

  def iterated[T](f: T => T): Stream[T => T] = {
    val id = (x: T) => x
    val transition: (T => T) => (T => T) = (g: T => T) => ((x: T) => f(g(x)))
    iterate[T => T](id)(transition)
  }

  def flatten(ls: List[Any]): List[Int] = {
    ls match {
      case Nil => Nil
      case x :: xr =>
        x match {
          case i: Int => i :: flatten(xr)
          case (y: List[Any]) => flatten(y) ++ flatten(xr)
          case _ => throw new Exception("Not List or Int")
        }
      case _ => throw new Exception("Not List or Int")
    }
  }
}