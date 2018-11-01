package example

import org.scalatest._

class HelloSpec extends FlatSpec with Matchers {
  "The Hello object" should "say hello" in {
    Hello.greeting shouldEqual "hello"
  }

  "fact(0)" should "return 1" in {
    Recitation1.factorial(0) shouldEqual 1
  }

  "fact(1)" should "return 1" in {
    Recitation1.factorial(1) shouldEqual 1
  }

  "fact(2)" should "return 2" in {
    Recitation1.factorial(2) shouldEqual 2
  }

  "sum(List(1, 2, 3))" should "return 6" in {
    Recitation1.sum(List(1, 2, 3)) shouldEqual 6
  }

  "fastExp(List(1, 2, 3))" should "return 6" in {
    Recitation1.fastExp(2, 3) shouldEqual 8
    Recitation1.fastExp(2, 4) shouldEqual 16
    Recitation1.fastExp(2, 5) shouldEqual 32
  }
}
