package example

import org.junit._
import org.junit.Assert.assertEquals

/**
 * This class implements a JUnit test suite for the methods in object
 * `Lists` that need to be implemented as part of this assignment. A test
 * suite is simply a collection of individual tests for some specific
 * component of a program.
 *
 * To run this test suite, start "sbt" then run the "test" command.
 */
 class ListsSuite {

  /**
   * Tests are written using the @Test annotation
   *
   * The most common way to implement a test body is using the method `assert`
   * which tests that its argument evaluates to `true`. So one of the simplest
   * successful tests is the following:
   */
  @Test def `one plus one is two`: Unit = {
    assert(1 + 1 == 2)
  }

  @Test def `one plus one is three?`: Unit = {
    assert(1 + 1 != 3)
  }

  /**
   * One problem with the previous (failing) test is that JUnit will
   * only tell you that a test failed, but it will not tell you what was
   * the reason for the failure. The output looks like this:
   *
   * {{{
   *    [info] - one plus one is three? *** FAILED ***
   * }}}
   *
   * This situation can be improved by using a Assert.assertEquals
   * (this is only possible in JUnit). So if you
   * run the next test, JUnit will show the following output:
   *
   * {{{
   *    [info] - details why one plus one is not three *** FAILED ***
   *    [info]   2 did not equal 3 (ListsSuite.scala:67)
   * }}}
   *
   * We recommend to always use the Assert.assertEquals equality operator
   * when writing tests.
   */
  @Test def `details why one plus one is not three`: Unit = {
    assertEquals(1 + 1, 2) // Fix me, please!
  }

  /**
   * Now we finally write some tests for the list functions that have to be
   * implemented for this assignment. We fist import all members of the
   * `List` object.
   */
  import Lists._


  /**
   * We only provide two very basic tests for you. Write more tests to make
   * sure your `sum` and `max` methods work as expected.
   *
   * In particular, write tests for corner cases: negative numbers, zeros,
   * empty lists, lists with repeated elements, etc.
   *
   * It is allowed to have multiple `assert` statements inside one test,
   * however it is recommended to write an individual `test` statement for
   * every tested aspect of a method.
   */
  @Test def `sum of a few numbers`: Unit = {
    assert(sum(List(1,2,0)) == 3)
  }

  @Test def `max of a few numbers`: Unit = {
    assert(max(List(3, 7, 2)) == 7)
  }



  @Rule def individualTestTimeout = new org.junit.rules.Timeout(1000)
}
