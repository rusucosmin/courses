import org.junit.Test
import org.junit.Assert._

class Test1 {
  @Test def t1(): Unit = {
    assertEquals("Hello, world!", Main.msg)
  }
}
