package objsets

import org.junit._
import org.junit.Assert.assertEquals

class TweetSetSuite {
  trait TestSets {
    val set1 = new Empty
    val set2 = set1.incl(new Tweet("a", "a body", 20))
    val set3 = set2.incl(new Tweet("b", "b body", 20))
    val c = new Tweet("c", "c body", 7)
    val d = new Tweet("d", "d body", 9)
    val set4c = set3.incl(c)
    val set4d = set3.incl(d)
    val set5 = set4c.incl(d)
    val set6 = set1.incl(new Tweet("e", "e body", 1))
        .incl(new Tweet("f", "f body", 2))
        .incl(new Tweet("g", "g body", 5))
        .incl(new Tweet("h", "h body", 7))
        .incl(new Tweet("bb", "bbbody", 100))
        .incl(new Tweet("cc", "ccbody", 12))
  }

  def asSet(tweets: TweetSet): Set[Tweet] = {
    var res = Set[Tweet]()
    tweets.foreach(res += _)
    res
  }

  def size(set: TweetSet): Int = asSet(set).size

  @Test def `filter: on empty set`: Unit =
    new TestSets {
      assertEquals(0, size(set1.filter(tw => tw.user == "a")))
    }

  @Test def `filter: on three nodes tree`: Unit =
    new TestSets {
      val set = new NonEmpty(new Tweet("a", "a", 1),
          new NonEmpty(new Tweet("b", "b", 2), new Empty, new Empty),
          new NonEmpty(new Tweet("c", "c", 3), new Empty, new Empty))
      val filteredSet = set.filter((_) => true)
      assertEquals(3, size(filteredSet))
    }


  @Test def `filter: a on set5`: Unit =
    new TestSets {
      assertEquals(1, size(set5.filter(tw => tw.user == "a")))
    }

  @Test def `filter: twenty on set5`: Unit =
    new TestSets {
      assertEquals(2, size(set5.filter(tw => tw.retweets == 20)))
    }

  @Test def `union: set4c and set4d`: Unit =
    new TestSets {
      assertEquals(4, size(set4c.union(set4d)))
    }

  @Test def `union: with empty set1`: Unit =
    new TestSets {
      assertEquals(4, size(set5.union(set1)))
    }

  @Test def `union: with empty set2`: Unit =
    new TestSets {
      assertEquals(4, size(set1.union(set5)))
    }

  @Test def `mostRetweeted: with set5`: Unit =
    new TestSets {
      val mostRetweeted = set5.mostRetweeted
      assertEquals(20, mostRetweeted.retweets)
    }

  @Test def `mostRetweeted: with empty set`: Unit =
    new TestSets {
      try {
        val mostRetweeted = set1.mostRetweeted
        assert(false)
      } catch {
        case e: NoSuchElementException => Unit;
      }
    }

  @Test def `mostRetweeted: with set2`: Unit =
    new TestSets {
      val mostRetweeted = set2.mostRetweeted
      assertEquals("a", mostRetweeted.user)
      assertEquals("a body", mostRetweeted.text)
      assertEquals(20, mostRetweeted.retweets)
    }

  @Test def `mostRetweeted: with set3`: Unit =
    new TestSets {
      val mostRetweeted = set3.mostRetweeted
      assertEquals(20, mostRetweeted.retweets)
    }

  @Test def `mostRetweeted: with set4c`: Unit =
    new TestSets {
      val mostRetweeted = set4c.mostRetweeted
      assertEquals(20, mostRetweeted.retweets)
    }

  @Test def `mostRetweeted: with set4d`: Unit =
    new TestSets {
      val mostRetweeted = set4c.mostRetweeted
      assertEquals(20, mostRetweeted.retweets)
    }


  @Test def `descending: set5`: Unit =
    new TestSets {
      val trends = set5.descendingByRetweet
      assert(!trends.isEmpty)
      assert(trends.head.user == "a" || trends.head.user == "b")
    }

  @Test def `descending: set6`: Unit =
    new TestSets {
      val trends = set6.descendingByRetweet
      assert(!trends.isEmpty)
      assert(trends.head.user == "bb" && trends.head.retweets == 100)
      assert(trends.tail.head.user == "cc" && trends.tail.head.retweets == 12)
    }

  @Test def `GoogleVsApple: googleSets is computed`: Unit =
    new TestSets {
      TweetReader.allTweets
      GoogleVsApple.googleTweets
      GoogleVsApple.appleTweets
      GoogleVsApple.trending
    }

  @Rule def individualTestTimeout = new org.junit.rules.Timeout(10 * 1000)
}
