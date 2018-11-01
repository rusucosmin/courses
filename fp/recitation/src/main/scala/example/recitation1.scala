package example

import scala.annotation._

object Recitation1 {
  //def factorial(n: Int): Int = if (n <= 0) 1 else n * factorial(n - 1)
  def factorial(n: Int): Int = {
    @tailrec
    def fact(n: Int, acc: Int): Int = {
      if (n <= 1) acc
      else fact(n - 1, acc * n)
    }
    fact(n, 1)
  }

  def sum(ls: List[Int]): Int = {
    @tailrec
    def _sum(ls: List[Int], acc: Int): Int = ls match {
      case Nil => acc
      case x :: xs => _sum(xs, x + acc)
    }
    _sum(ls, 0)
  }

  def fastExp(base: Int, n: Int): Int = {
    @tailrec
    def _fastExp(base: Int, n: Int, acc: Int): Int = {
      if (n == 0) acc
      else if(n == 1) acc * base
      else if (n % 2 == 0) _fastExp(base * base, n / 2, acc)
      else _fastExp(base * base, n / 2, acc * base)
    }
    _fastExp(base, n, 1)
  }

  def fibonacci(n: Int): Int = {
    @tailrec
    def fibo(n: Int, a: Int, b: Int): Int = {
      if (n == 0) a
      else if(n == 1) b
      else fibo(n - 1, b, a + b)
    }
    fibo(n, 1, 1)
  }
}