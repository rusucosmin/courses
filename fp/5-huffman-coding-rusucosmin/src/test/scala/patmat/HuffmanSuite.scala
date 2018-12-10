package patmat

import org.junit._
import org.junit.Assert.assertEquals

class HuffmanSuite {
  import Huffman._

  trait TestTrees {
    val t1 = Fork(Leaf('a',2), Leaf('b',3), List('a','b'), 5)
    val t2 = Fork(Fork(Leaf('a',2), Leaf('b',3), List('a','b'), 5), Leaf('d',4), List('a','b','d'), 9)
  }


  @Test def `weight of a larger tree`: Unit =
    new TestTrees {
      assertEquals(5, weight(t1))
    }

  @Test def `chars of a larger tree`: Unit =
    new TestTrees {
      assertEquals(List('a','b','d'), chars(t2))
    }

  @Test def `string2chars hello world`: Unit =
    assertEquals(List('h', 'e', 'l', 'l', 'o', ',', ' ', 'w', 'o', 'r', 'l', 'd'), string2Chars("hello, world"))


  @Test def `make ordered leaf list for some frequency table`: Unit =
    assertEquals(List(Leaf('e',1), Leaf('t',2), Leaf('x',3)), makeOrderedLeafList(List(('t', 2), ('e', 1), ('x', 3))))


  @Test def `combine of some leaf list`: Unit = {
    val leaflist = List(Leaf('e', 1), Leaf('t', 2), Leaf('x', 4))
    assertEquals(List(Fork(Leaf('e',1),Leaf('t',2),List('e', 't'),3), Leaf('x',4)), combine(leaflist))
  }

  @Test def `decode and encode a very short text should be identity`: Unit =
    new TestTrees {
      assertEquals("ab".toList, decode(t1, encode(t1)("ab".toList)))
    }

  @Test def `simple createCodeTree`: Unit = {
    new TestTrees {
      assertEquals(createCodeTree(List('a', 'b')), Fork(Leaf('a', 1), Leaf('b', 1), List('a', 'b'), 2))
    }
  }

  @Test def `createCodeTree aba`: Unit = {
    new TestTrees {
      assertEquals(createCodeTree(List('a', 'b', 'a')), Fork(Leaf('b', 1), Leaf('a', 2), List('b', 'a'), 3))
    }
  }
  
  @Test def `encode frenchCode`: Unit = {
    new TestTrees {
      assertEquals(encode(frenchCode)("huffmanestcool".toList), secret)
    }
  }

  @Test def `encode and decode using frenchCode should be identity`: Unit = {
    new TestTrees {
      assertEquals(decode(frenchCode, encode(frenchCode)("huffmanestcool".toList)), "huffmanestcool".toList)
    }
  }

  @Test def `quickEncode and decode using frenchCode should be identity`: Unit = {
    new TestTrees {
      assertEquals(decode(frenchCode, quickEncode(frenchCode)("huffmanestcool".toList)), "huffmanestcool".toList)
    }
  }

  @Test def `decode frenchCode`: Unit = {
    new TestTrees {
      assertEquals(decode(frenchCode, secret), "huffmanestcool".toList)
    }
  }

  @Test def `quickEncode frenchCode`: Unit = {
    new TestTrees {
      assertEquals(quickEncode(frenchCode)("huffmanestcool".toList), secret)
    }
  }


  @Rule def individualTestTimeout = new org.junit.rules.Timeout(10 * 1000)
}
