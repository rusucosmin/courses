package forcomp

import org.junit._
import org.junit.Assert.assertEquals


class AnagramsSuite {
  import Anagrams._

  @Test def `wordOccurrences abcd`: Unit =
    assertEquals(List(('a', 1), ('b', 1), ('c', 1), ('d', 1)), wordOccurrences("abcd"))

  @Test def `wordOccurrences robert`: Unit =
    assertEquals(List(('b', 1), ('e', 1), ('o', 1), ('r', 2), ('t', 1)), wordOccurrences("Robert"))

  @Test def `sentenceOccurrences abcd e`: Unit =
    assertEquals(List(('a', 1), ('b', 1), ('c', 1), ('d', 1), ('e', 1)), sentenceOccurrences(List("abcd", "e")))

  @Test def `wordAnagrams married`: Unit =
    assertEquals(Set("married", "admirer"), wordAnagrams("married").toSet)

  @Test def `wordAnagrams player`: Unit =
    assertEquals(Set("parley", "pearly", "player", "replay"), wordAnagrams("player").toSet)


  @Test def `dictionaryByOccurrences.get: eat`: Unit =
    assertEquals(Some(Set("ate", "eat", "tea")), dictionaryByOccurrences.get(List(('a', 1), ('e', 1), ('t', 1))).map(_.toSet))



  @Test def `subtract: lard - r`: Unit = {
    val lard = List(('a', 1), ('d', 1), ('l', 1), ('r', 1))
    val r = List(('r', 1))
    val lad = List(('a', 1), ('d', 1), ('l', 1))
    assertEquals(lad, subtract(lard, r))
  }

  @Test def `subtract: lard - m`: Unit = {
    val lard = List(('a', 2), ('d', 1), ('l', 1), ('r', 1))
    val m = List(('r', 1), ('a', 1))
    val lad = List(('a', 1), ('d', 1), ('l', 1))
    assertEquals(lad, subtract(lard, m))
  }

  @Test def `combinations: []`: Unit =
    assertEquals(List(Nil), combinations(Nil))

  @Test def `combinations: abba`: Unit = {
    val abba = List(('a', 2), ('b', 2))
    val abbacomb = List(
      List(),
      List(('a', 1)),
      List(('a', 2)),
      List(('b', 1)),
      List(('a', 1), ('b', 1)),
      List(('a', 2), ('b', 1)),
      List(('b', 2)),
      List(('a', 1), ('b', 2)),
      List(('a', 2), ('b', 2))
    )
    val comb = combinations(abba)
    assertEquals(abbacomb.length, comb.length)
    assertEquals(abbacomb.toSet, comb.toSet)
  }


  @Test def `sentence anagrams: []`: Unit = {
    val sentence = List()
    assertEquals(List(Nil), sentenceAnagrams(sentence))
  }

  @Test def `sentence anagrams: Linux`: Unit = {
    val sentence = List("Linux")
    val anas = List(
      List("Linux")
    )
    assertEquals(anas.toSet, sentenceAnagrams(sentence).toSet)
  }

  @Test def `sentence anagrams: Linux rulez`: Unit = {
    val sentence = List("Linux", "rulez")
    val anas = List(
      List("Rex", "Lin", "Zulu"),
      List("nil", "Zulu", "Rex"),
      List("Rex", "nil", "Zulu"),
      List("Zulu", "Rex", "Lin"),
      List("null", "Uzi", "Rex"),
      List("Rex", "Zulu", "Lin"),
      List("Uzi", "null", "Rex"),
      List("Rex", "null", "Uzi"),
      List("null", "Rex", "Uzi"),
      List("Lin", "Rex", "Zulu"),
      List("nil", "Rex", "Zulu"),
      List("Rex", "Uzi", "null"),
      List("Rex", "Zulu", "nil"),
      List("Zulu", "Rex", "nil"),
      List("Zulu", "Lin", "Rex"),
      List("Lin", "Zulu", "Rex"),
      List("Uzi", "Rex", "null"),
      List("Zulu", "nil", "Rex"),
      List("rulez", "Linux"),
      List("Linux", "rulez")
    )
    assertEquals(anas.toSet, sentenceAnagrams(sentence).toSet)
  }


  @Rule def individualTestTimeout = new org.junit.rules.Timeout(10 * 1000)
}
