package interpreter
import Lisp._

object Main {
  import java.io.{BufferedReader, InputStreamReader}
  val in = new BufferedReader(new InputStreamReader(System.in))

  def main(args: Array[String]): Unit = {
    val userInput = scala.io.StdIn.readLine("  lisp> ")
    if (userInput.contains("exit") || userInput.contains("quit")) {
      println("byebye")
    } else {
      println(s"${lisp2string(evaluate(userInput))}")
      main(args)
    }
  }
}

object LispCode {
  // From a list (a, b, c, d) it should compute (d, c, b, a)
  // Write it as a String, and test it in your REPL
  val reverse = """
  def (reverse L acc)
    (if (null? L) acc (reverse (cdr L) (cons (car L) acc)) )
  """

  // From a list (a, b, c, d ...) it should compute (a, b-a, c-b, d-c ...)
  // You might find useful to define an inner loop def
  val differences = """
    def (differences l)
      (def (reverse L acc) acc
      (def (reverse L acc)
        (if (null? L) acc (reverse (cdr L) (cons (car L) acc)) )
      (def differencesAux (lambda (L acc)
        (if (null? L)
          (reverse acc nil)
          (if (null? (cdr L)) (reverse acc nil) (differencesAux (cdr L) (cons (- (car (cdr L)) (car L)) acc)))
          )
        )
      (
        if (null? l) l (cons (car l) (differencesAux l nil))))
      ))
  """
  val rebuildList = """
    def (rebuildList l)
      (def (rebuildListAux L)
        (if (null? L) nil
        (if (null? (cdr L)) nil
        (val x (car L) (val y (car (cdr L)) (val sum (+ x y) (cons sum (rebuildListAux (cons sum (cdr (cdr L))))))))))
      (if (null? l) nil (cons (car l) (rebuildListAux l))))
  """



  val withDifferences: String => String =
    (code: String) => "(" + reverse + " (" + differences + " (" + rebuildList + " " + code + ")))"
}
