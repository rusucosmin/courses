package example

import scala.annotation._

object Recitation2 {
  def flip(f: (Int, Double) => Int): (Double, Int) => Int = (x, y) => f(y, x)
  val id: Int => Int = x => x
  def compose(f: Int => Int, g: Int => Int): Int => Int = x => f(g(x))
  def repeated(f: Int => Int, n: Int): Int => Int = {
    if (n == 0) x => x
    else x => f(repeated(f, n - 1)(x))
  }
}