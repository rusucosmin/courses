package example

import org.scalatest._

class HelloSpec extends FlatSpec with Matchers {
  "The Hello object" should "say hello" in {
    Hello.greeting shouldEqual "hello"
  }

  "Test Array without order" should "pass" in {
    List(("a", 2), ("b", 3), ("c", 4)) should contain theSameElementsAs List(("a", 2), ("b", 3), ("c", 4))
    List(List("a", 2), List("b", 3), List("c", 4)).flatten should contain theSameElementsAs List(("a", 2), ("b", 3), ("c", 4))
  }
}
