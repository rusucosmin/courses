package example

import scala.annotation._

object Recitation3 {
  val intLeq = (x: Int, y: Int) => x <= y
  val emptyIntTree: Tree[Int] = new EmptyTree(intLeq)
}

abstract class Tree[T] {
  def size: Int
  def treeSize: Int = this match {
    case EmptyTree(leq) => 0
    case Node(left, elem, right, leq) => 1 + left.size + right.size
  }
  def add(t: T): Tree[T] = this match {
    case EmptyTree(leq) => Node(EmptyTree(leq), t, EmptyTree(leq), leq)
    case Node(left, elem, right, leq) => {
      if (t == elem) this
      else if (leq(t, elem)) Node(left add t, elem, right, leq)
      else Node(left, elem, right add t, leq)
    }
  }
  def toList: List[T] = {
    def concat[T](a: List[T], b: List[T]): List[T] = a match {
      case Nil => b
      case x :: xs => x :: concat(xs, b)
    }
    this match {
      case EmptyTree(leq) => Nil
      case Node(left, elem, right, leq) => concat(concat(left.toList, List(elem)), right.toList)
    }
  }
  def toSortedList[T](leq: (T, T) => Boolean, ls: List[T]): List[T] = {
    def buildTree(ls: List[T], t: Tree[T]): Tree[T] = ls match {
      case Nil => t
      case x :: xs => buildTree(xs, t.add(x))
    }
    buildTree(ls, EmptyTree(leq)).toList
  }
}
case class EmptyTree[T](leq: (T, T) => Boolean) extends Tree[T] {
  def size = 0
}
case class Node[T](left: Tree[T], elem: T, right: Tree[T], leq: (T, T) => Boolean) extends Tree[T] {
  def size: Int = left.size + right.size + 1
}