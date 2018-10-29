package example

object Mid2016 extends Mid2016 with App {
}

trait Mid2016 {
  def scanLeft[A, B](xs: List[A])(z: B)(op: (B, A) => B): List[B] =
    xs.foldLeft(List(z))((list:List[B], x: A) => op(list.head, x) :: list).reverse.tail

  def flatMap[A, B](xs: List[A])(f: A => List[B]): List[B] = {
    xs.foldRight(List[B]())((x: A, y: List[B]) => f(x).foldRight(y)(_ :: _))
  }

  def reachable(n: Int, init: Set[Node], edges: List[Edge]): Set[Node] = {
    if (n == 0) init
    else reachable(n - 1, init.toList.flatMap((x) => edges.filter(_.from == x).map(_.to)).toSet, edges)
  }

  def cycles3(nodes: Set[Node], edges: List[Edge]): Set[Node] = {
    val reach = reachable(3, nodes, edges)
    nodes.filter((x) => reachable(3, Set(x), edges).filter(_ == x).nonEmpty)
  }
}

case class Node(id: Int)
case class Edge(from: Node, to: Node)
