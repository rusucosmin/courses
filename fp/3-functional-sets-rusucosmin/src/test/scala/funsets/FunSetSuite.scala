package funsets

import org.junit._

/**
 * This class is a test suite for the methods in object FunSets.
 *
 * To run this test suite, start "sbt" then run the "test" command.
 */
class FunSetSuite {

  import FunSets._

  @Test def `contains is implemented`: Unit = {
    assert(contains(x => true, 100))
  }
  
  /**
   * When writing tests, one would often like to re-use certain values for multiple
   * tests. For instance, we would like to create an Int-set and have multiple test
   * about it.
   *
   * Instead of copy-pasting the code for creating the set into every test, we can
   * store it in the test class using a val:
   *
   *   val s1 = singletonSet(1)
   *
   * However, what happens if the method "singletonSet" has a bug and crashes? Then
   * the test methods are not even executed, because creating an instance of the
   * test class fails!
   *
   * Therefore, we put the shared values into a separate trait (traits are like
   * abstract classes), and create an instance inside each test method.
   *
   */

  trait TestSets {
    val s1 = singletonSet(1)
    val s2 = singletonSet(2)
    val s3 = singletonSet(3)
  }

  /**
   * This test is currently disabled (by using @Ignore) because the method
   * "singletonSet" is not yet implemented and the test would fail.
   *
   * Once you finish your implementation of "singletonSet", remove the
   * @Ignore annotation.
   */
   @Test def `singleton set one contains one`: Unit = {

    /**
     * We create a new instance of the "TestSets" trait, this gives us access
     * to the values "s1" to "s3".
     */
    new TestSets {
      /**
       * The string argument of "assert" is a message that is printed in case
       * the test fails. This helps identifying which assertion failed.
       */
      assert(contains(s1, 1), "Singleton1")
      assert(contains(s2, 2), "Singleton2")
      assert(contains(s3, 3), "Singleton3")
    }
  }

  @Test def `singleton does not contains anything else`: Unit = {

    /**
     * We create a new instance of the "TestSets" trait, this gives us access
     * to the values "s1" to "s3".
     */
    new TestSets {
      /**
       * The string argument of "assert" is a message that is printed in case
       * the test fails. This helps identifying which assertion failed.
       */
      assert(!contains(s1, 2), "NotSingleton1_2")
      assert(!contains(s1, 3), "NotSingleton1_3")
      assert(!contains(s2, 1), "NotSingleton2_1")
      assert(!contains(s2, 3), "NotSingleton2_3")
      assert(!contains(s3, 1), "NotSingleton3_1")
      assert(!contains(s3, 2), "NotSingleton3_2")
    }
  }

  @Test def `union contains all elements of each set`: Unit = {
    new TestSets {
      val s = union(s1, s2)
      assert(contains(s, 1), "Union 1")
      assert(contains(s, 2), "Union 2")
      assert(!contains(s, 3), "Union 3")
    }
  }
  @Test def `intersect contains all common elements of sets`: Unit = {
    new TestSets {
      val s = intersect(union(s1, s2), union(s2, s3))
      assert(contains(s, 2), "Interesect 1")
      assert(!contains(s, 1), "Intersect 2")
      assert(!contains(s, 3), "Intersect 3")
    }
  }

  @Test def `diff contains all elements of first set that are not in second`: Unit = {
    new TestSets {
      val s = diff(union(s1, s2), s2)
      assert(contains(s, 1), "Diff 1")
      assert(!contains(s, 2), "Diff 2")
      assert(!contains(s, 3), "Diff 3")
    }
  }

  @Test def `Filter contains all subsets that mathc the predicate`: Unit = {
    new TestSets {
      val s = filter(union(s1, s2), x => x % 2 == 0)
      assert(!contains(s, 1), "Filter 1")
      assert(contains(s, 2), "Filter 2")
    }
  }

  @Test def `For all is true on always true predicate`: Unit = {
    new TestSets {
      assert(forall(s1, _ => true), "Forall 1")
      assert(forall(s2, _ => true), "Forall 2")
      assert(forall(s3, _ => true), "Forall 3")
    }
  }

  @Test def `For all is not true on parity check`: Unit = {
    new TestSets {
      assert(!forall(union(s1, s2), x => x % 2 == 0), "Forall 1")
      assert(!forall(union(s1, s2), x => x % 2 == 1), "Forall 2")
    }
  }

  @Test def `Exists performs as needed`: Unit = {
    new TestSets {
      assert(exists(union(s1, s2), x => x % 2 == 0), "Exists 1")
      assert(exists(union(s1, s2), x => x % 2 == 1), "Exists 2")
      assert(!exists(union(s1, s2), x => x == 3), "Exists 3")
    }
  }

  @Test def `Map performs as intended`: Unit = {
    new TestSets {
      val s = map(union(s1, s2), x => x + 1)
      assert(contains(s, 2), "Map")
      assert(contains(s, 3), "Map")
    }
  }

  @Rule def individualTestTimeout = new org.junit.rules.Timeout(10 * 1000)
}

