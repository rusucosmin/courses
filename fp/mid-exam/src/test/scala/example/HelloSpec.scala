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

  "Difference on nil" should "be nil" in {
    Mid2015.differences(Nil) shouldEqual Nil
  }

  "Difference on one-element list" should "be that element" in {
    Mid2015.differences(List(1)) shouldEqual List(1)
  }

  "Difference on general list" should "be correct" in {
    Mid2015.differences(List(1, 2)) shouldEqual List(1, 1)
  }

  "difference on longer test" should "be correct" in {
    Mid2015.differences(List(1, -2, 3, -4, 5, -6)) shouldEqual List(1, -3, 5, -7, 9, -11)
  }

  "rebList1" should "work" in {
    Mid2015.rebuildList(Nil) shouldEqual Nil
  }

  "rebList2" should "work" in {
    Mid2015.rebuildList(List(1)) shouldEqual List(1)
  }

  "rebList3" should "work" in {
    Mid2015.rebuildList(Mid2015.differences(List(1, -2, 3, -4, 5, -6))) shouldEqual List(1, -2, 3, -4, 5, -6)
  }

}
