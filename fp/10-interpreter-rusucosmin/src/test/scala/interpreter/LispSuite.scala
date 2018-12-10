package interpreter

import org.junit._
import org.junit.Assert.assertEquals
import Lisp._

class LispSuite extends {
  val expr1 = "(+ 1 2)"

  @Test def addition: Unit = {
    assertEquals(string2lisp(expr1).toString, "List('+, 1, 2)")
    assertEquals(evaluate(expr1), 3)
  }

  val expr2 = "((lambda(x) (+ x 1)) 41)"

  @Test def expr2test: Unit = {
    val expectedStructure = "List(List('lambda, List('x), List('+, 'x, 1)), 41)"
    assertEquals(expectedStructure, string2lisp(expr2).toString)
    assertEquals(42, evaluate(expr2))
  }

  val expr3 =
    """
      (val g (lambda (x) (x 2))
        (val f (lambda (x) (g (lambda(y) (+ x y))))
          (f 1)))
    """

  @Test def expr3test: Unit = {
    val expectedStructure = "List('val, 'g, List('lambda, List('x), List('x, 2)), List('val, 'f, List('lambda, List('x), List('g, List('lambda, List('y), List('+, 'x, 'y)))), List('f, 1)))"
    assertEquals(expectedStructure, string2lisp(expr3).toString)
    assertEquals(3, evaluate(expr3))
  }

  val expr4 =
    """
      (val g (lambda (z) (z 2))
        (val f (lambda (x) (g (lambda(y) (+ x y))))
          (f 1)))
    """

  @Test def expr4test: Unit = {
    val expectedStructure = "List('val, 'g, List('lambda, List('z), List('z, 2)), List('val, 'f, List('lambda, List('x), List('g, List('lambda, List('y), List('+, 'x, 'y)))), List('f, 1)))"
    assertEquals(expectedStructure, string2lisp(expr4).toString)
    assertEquals(3, evaluate(expr4))
  }

  val factDef =
    """
      def factorial (lambda (n)
        (if (= n 0)
            1
            (* n (factorial (- n 1)))))
    """

  def expr5 = s"($factDef(factorial 4))"

  @Test def expr5test: Unit = {
    val expectedStructure = "List('def, 'factorial, List('lambda, List('n), List('if, List('=, 'n, 0), 1, List('*, 'n, List('factorial, List('-, 'n, 1))))), List('factorial, 4))"
    assertEquals(expectedStructure, string2lisp(expr5).toString)
    assertEquals(24, evaluate(expr5))
  }

  val factDefSugar =
    """
      def (factorial n)
        (if (= n 0)
            1
            (* n (factorial (- n 1))))
    """

  def expr6 = s"($factDefSugar(factorial 4))"

  @Test def defSugar1: Unit =
    assertEquals(24, evaluate(expr6))

  @Test def defSugar2: Unit =
    assertEquals(3, evaluate("(def (add a b) (+ a b) (add 1 2))"))

  @Test def defSugar3: Unit =
    assertEquals(1, evaluate("(def (succ x) (+ x 1) (succ 0))"))

  @Test def defSugar4: Unit =
    assertEquals(0, evaluate("(def (foo) 0 (foo))"))

  @Test def caseSugar1: Unit =
    assertEquals(2, evaluate("(case 1 (else 2))"))

  @Test def caseSugar2: Unit =
    assertEquals(3, evaluate("(case 1 (1 3) (else 4))"))

  @Test def caseSugar3: Unit =
    assertEquals(4, evaluate("(case 2 (1 3) (else 4))"))

  @Test def caseSugar4: Unit =
    assertEquals(12, evaluate("(case 2 (1 11) (2 12) (3 13) (else 14))"))

  @Test def caseSugar5: Unit =
    assertEquals(100, evaluate("(case (case 1 (2 50) (3 4) (else 5)) (3 51) (5 100) (else 0))"))

  @Test def sugar1: Unit =
    assertEquals(1, evaluate("(def (yo a) (case a (1 a) (else 1)) (yo 2))"))

  @Test def differencesLisp1: Unit =
    assertEquals(List(), evaluate(LispCode.withDifferences("(differences nil)")))

  @Test def differencesLisp2: Unit =
    assertEquals(List(7), evaluate(LispCode.withDifferences("(differences (cons 7 nil))")))

  @Test def differencesLisp3: Unit =
    assertEquals(List(0, 0, 0), evaluate(LispCode.withDifferences("(differences (cons 0 (cons 0 (cons 0 nil))))")))

  @Test def differencesLisp4: Unit =
    assertEquals(List(1, 1, 1), evaluate(LispCode.withDifferences("(differences (cons 1 (cons 2 (cons 3 nil))))")))

  @Test def differencesLisp5: Unit =
    assertEquals(List(4, -3, 5), evaluate(LispCode.withDifferences("(differences (cons 4 (cons 1 (cons 6 nil))))")))

  @Test def rebuildListLisp1: Unit =
    assertEquals(List(), evaluate(LispCode.withDifferences("(rebuildList nil)")))

  @Test def rebuildListLisp2: Unit =
    assertEquals(List(7), evaluate(LispCode.withDifferences("(rebuildList (cons 7 nil))")))

  @Test def rebuildListLisp3: Unit =
    assertEquals(List(0, 0, 0), evaluate(LispCode.withDifferences("(rebuildList (cons 0 (cons 0 (cons 0 nil))))")))

  @Test def rebuildListLisp4: Unit =
    assertEquals(List(1, 2, 3), evaluate(LispCode.withDifferences("(rebuildList (cons 1 (cons 1 (cons 1 nil))))")))

  @Test def rebuildListLisp5: Unit =
    assertEquals(List(4, 1, 6), evaluate(LispCode.withDifferences("(rebuildList (cons 4 (cons -3 (cons 5 nil))))")))
}

