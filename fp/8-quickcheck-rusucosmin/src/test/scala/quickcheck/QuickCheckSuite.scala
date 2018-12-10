package quickcheck

import org.scalacheck.Properties

import org.junit._

import org.scalacheck.Arbitrary._
import org.scalacheck.Prop
import org.scalacheck.Prop._
import org.scalacheck.Test.{check, Result, Failed, PropException}

object QuickCheckBinomialHeap extends QuickCheckHeap with BinomialHeap

class QuickCheckSuite {
  def checkBogus(p: Properties): Unit = {
    def fail = throw new AssertionError(
      s"A bogus heap should NOT satisfy all properties. Try to find the bug!")

    check(asOneProperty(p))(identity) match {
      case r: Result => r.status match {
        case _: Failed         => () // OK: scalacheck found a counter example!
        case p: PropException  => p.e match {
          case e: NoSuchElementException => () // OK: the implementation throws NSEE
          case _ => fail
        }
        case _ => fail
      }
    }
  }

  /** Turns a `Properties` instance into a single `Prop` by combining all the properties */
  def asOneProperty(properties: Properties): Prop = Prop.all(properties.properties.map(_._2):_*)

  @Test def `Binomial heap satisfies properties.`: Unit =
    check(asOneProperty(new QuickCheckHeap with quickcheck.test.BinomialHeap))(identity)

  @Test def `Bogus (1) binomial heap does not satisfy properties.`: Unit =
    checkBogus(new QuickCheckHeap with quickcheck.test.Bogus1BinomialHeap)

  @Test def `Bogus (2) binomial heap does not satisfy properties.`: Unit =
    checkBogus(new QuickCheckHeap with quickcheck.test.Bogus2BinomialHeap)

  @Test def `Bogus (3) binomial heap does not satisfy properties.`: Unit =
    checkBogus(new QuickCheckHeap with quickcheck.test.Bogus3BinomialHeap)

  @Test def `Bogus (4) binomial heap does not satisfy properties.`: Unit =
    checkBogus(new QuickCheckHeap with quickcheck.test.Bogus4BinomialHeap)

  @Test def `Bogus (5) binomial heap does not satisfy properties.`: Unit =
    checkBogus(new QuickCheckHeap with quickcheck.test.Bogus5BinomialHeap)

  @Rule def individualTestTimeout = new org.junit.rules.Timeout(10 * 1000)
}
