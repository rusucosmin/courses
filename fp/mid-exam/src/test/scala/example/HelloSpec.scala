package example

import org.scalatest._

class HelloSpec extends FlatSpec with Matchers {
  "Mid2016 scanLeft" should "return correct results" in {
    Mid2016.scanLeft(List("A", "B", "C"))("z")(_ + _) shouldEqual List("zA", "zAB", "zABC")
    Mid2016.scanLeft(List("A"))("z")(_ + _) shouldEqual List("zA")
    Mid2016.scanLeft(List())("z")(_ + _) shouldEqual List()
  }

  "Mid2016 flatMap" should "return correct results" in {
    Mid2016.flatMap(List("Ana", "are", "mere"))((x: String) => x.toList) shouldEqual "Anaaremere".toList
  }

  "Reachable should be correctly implemented" should "return correct results" in {
    Mid2016.reachable(1, Set(Node(1)),List(Edge(Node(1), Node(2)))) shouldEqual Set(Node(2))
    Mid2016.reachable(2, Set(Node(1)),List(Edge(Node(1), Node(2)), Edge(Node(2), Node(1)))) shouldEqual Set(Node(1))
  }

  "Cycle 3 should detect 3 cycles" should "return correct results" in {
    Mid2016.cycles3(Set(Node(1)), List(Edge(Node(1), Node(2)))) shouldEqual Set()
    Mid2016.cycles3(Set(Node(1)), List(Edge(Node(1), Node(2)), Edge(Node(2), Node(3)), Edge(Node(3), Node(1)))) shouldEqual Set(Node(1))
    Mid2016.cycles3(Set(Node(1), Node(2), Node(3)), List(Edge(Node(1), Node(2)), Edge(Node(2), Node(3)), Edge(Node(3), Node(1)))) shouldEqual Set(Node(1), Node(2), Node(3))
  }
}
