// Note: "Run this worksheet" does not recompile other files in this project,
// You should run "~compile" in sbt to automatically recompile the project.

import interpreter._
import Lisp._

// Uncomment to enable tracing of each evaluation step
// trace = true

var factorial = """
(def factorial
  (lambda (n)
    (if (= n 0)
      1
      (* n (factorial (- n 1)))))
  (factorial 5))
"""

println(evaluate(factorial))

def derive(x: Symbol, expr: Any): Any = expr match {
  case List('+, f, g) =>
    List('+, derive(x, f), derive(x, g))
  case List('*, f, g) =>
    List('+, List('*, derive(x, f), g), List('*, f, derive(x, g)))
  case _ => if (x == expr) 1 else 0;
}

derive('x, List('+, 'y, List('+, 2, 'x)))

val lispEx2 = """
  (def (derive x expr) expr
    (if (isCons? expr)
      (if (= '+ (nth 0 expr))
        (list '+ (derive x (nth 1 expr)) (derive x (nth 2 expr)))
        (list '+ (list '* (derive x (nth 1 expr)) (nth 2 expr))
          (list '* (nth 1 expr) (derive x (nth 2 expr)))))
      (if (= expr x) 1 0)) 
  rest)
"""
println(evaluate(lispEx2))

def testStartsWith(input: Stream[Char], pattern: List[Char]): Option[Stream[Char]] = {
  if (input.take(pattern.length) == pattern) Some(input.drop(pattern.length))
  else None
}

assert(testStartsWith(Stream('a', 'b', 'c'), List('a', 'b')) == Some(Stream('c')))
assert(testStartsWith(Stream('a', 'b', 'c'), List('b', 'c')) == None)
assert(testStartsWith('a' #:: 'b' #:: Stream('c', 'd', 'e'), List('a')) == Some('b' #:: 'c' #:: Stream('d', 'e')))

def replaceAll(input: Stream[Char], pattern: List[Char], replacement: List[Char]): Stream[Char] = {
  testStartsWith(input, pattern) match {
    case Some(rest) => replaceAll(replacement.toStream #::: rest, pattern, replacement)
    case None => if (input.isEmpty) Stream.empty
      else input.head #:: replaceAll(input.tail, pattern, replacement)
  }
}

assert(replaceAll(Stream('a', 'a', 'a'), List('a', 'a'), List('b')) == Stream('b', 'a'))
assert(replaceAll(Stream('a', 'a', 'b', 'a', 'b', 'a'), List('a', 'b', 'a'), List('b', 'a')) == Stream('a', 'b', 'b', 'a'))

def replaceAllMany(input: Stream[Char], patternsAndReplacements: List[(List[Char], List[Char])]): Stream[Char] = {
  def _replaceAux(input: Stream[Char], par: List[(List[Char], List[Char])]): Stream[Char] = {
    par match {
      case (pattern, replacement) :: rest =>
        testStartsWith(input, pattern) match {
          case Some(restStream) => _replaceAux(replacement.toStream #::: restStream, patternsAndReplacements)
          case None =>
            if (input.isEmpty) Stream.empty
            else _replaceAux(input, rest)
        }
      case Nil =>
        if (input.isEmpty) Stream.empty
        else input.head #:: _replaceAux(input.tail, patternsAndReplacements)
    }
  }
  _replaceAux(input, patternsAndReplacements)
}

assert(replaceAllMany(Stream('a', 'a', 'b', 'b'), List(
  (List('a', 'b'), List('c')),
  (List('a', 'a'), List('d')))) == Stream('d', 'b', 'b'))
assert(replaceAllMany(Stream('d', 'a', 'a', 'a', 'b', 'b'), List(
  (List('e', 'b'), List('c')),
  (List('a', 'a', 'a'), List('d', 'e')),
  (List('d', 'd'), List('z')))) == Stream('d', 'd', 'c', 'b'))
println(replaceAllMany(Stream('a', 'a', 'b', 'b'), List(
  (List('a', 'b'), List('c')),
  (List('a', 'a'), List('d')))).take(100).toList)
println(replaceAllMany(Stream('d', 'a', 'a', 'a', 'b', 'b'), List(
  (List('e', 'b'), List('c')),
  (List('a', 'a', 'a'), List('d', 'e')),
  (List('d', 'd'), List('z')))).take(100).toList)

def pairAverages(data: Stream[Double]): Stream[Double] = data match {
  case a #:: b #:: rest => ((a + b) / 2) #:: pairAverages(b #:: rest)
  case _ => Stream.empty
}

assert(pairAverages(Stream[Double](1, 1, 4, 5, 7, 0)) == Stream[Double](1, 2.5, 4.5, 6, 3.5))
assert(pairAverages(Stream.Empty) == Stream.Empty)
assert(pairAverages(Stream[Double](1)) == Stream.Empty)
assert(pairAverages(Stream[Double](1, 1)) == Stream[Double](1))
assert(pairAverages(Stream[Double](1, 1, 2)) == Stream[Double](1, 1.5))

def windowAverage(windowSize: Double, data: Stream[Double]): Stream[Double] = {
  val x: List[Double] = data.take(windowSize.toInt).toList
  if (x.length == windowSize) (x.reduce(_ + _).toDouble / windowSize) #:: windowAverage(windowSize, data.tail)
  else Stream.empty
}

def ~=(x: Stream[Double], y: Stream[Double], precision: Double = 0.1): Boolean = (x, y) match {
  case (Stream.Empty, Stream.Empty) => true
  case (x, Stream.Empty) => false
  case (Stream.Empty, x) => false
  case (x #:: xs, y #:: ys) => if ((x - y).abs < precision) ~=(xs, ys, precision) else false
}

assert(windowAverage(2, Stream[Double](1, 1, 4, 5, 7)) == Stream[Double](1, 2.5, 4.5, 6))
assert(~=(windowAverage(3, Stream[Double](1, 2, 5, 8, 15)), Stream[Double](2.67, 5, 9.33)))

def rollingAverage(data: Stream[Double]): Stream[Double] = {
  def _rollingAverage(data: Stream[Double], sumSoFar: Double, numberOfElements: Int): Stream[Double] = data match {
    case Stream.Empty => Stream.Empty
    case x #:: rest => ((sumSoFar + x) / (numberOfElements + 1)) #:: _rollingAverage(rest, sumSoFar + x, numberOfElements + 1)
  }
  _rollingAverage(data, 0.0, 0)
}

assert(rollingAverage(Stream(1, 2, 3, 4, 5)) == Stream(1, 1.5, 2, 2.5, 3))

def substitute(term: Any, symbol: Symbol, replaceBy: Any): Any = term match {
  case xs: List[Any] => xs.map(substitute(_, symbol, replaceBy))
  case _ => if (term == symbol) replaceBy else term
}

substitute(List('+, 'a, List('+, 2, 'a)), 'a, 1)

val x= """
  (def (substitute term symbol replaceBy)
    (if (isCons? term)
      (cons (substitute (car term) symbol replaceBy) (substitute (cdr term) symbol replaceBy))
      (if (= term symbol) replaceBy term)) 
  rest)
"""

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
println(evaluate(s"($differences(differences nil))"))
println(evaluate(s"($differences(differences (cons 1 nil)))"))
println(evaluate(s"($differences(differences (cons 1 (cons 2 nil))))"))
println(evaluate(s"($differences(differences (cons 1 (cons 2 (cons 3 nil)))))"))
println(evaluate(s"($differences(differences (cons 1 (cons 2 (cons 3 (cons 5 nil))))))"))
println(evaluate(s"($differences(differences (cons 4 (cons 2 (cons 3 (cons 5 nil))))))"))
val rebuildList = """
  def (rebuildList l)
    (def (rebuildListAux L)
      (if (null? L) nil
      (if (null? (cdr L)) nil
      (val x (car L) (val y (car (cdr L)) (val sum (+ x y) (cons sum (rebuildListAux (cons sum (cdr (cdr L))))))))))
    (if (null? l) nil (cons (car l) (rebuildListAux l))))
  """
println(evaluate(s"($rebuildList(rebuildList (cons 1 (cons 2 nil))))"))
println(evaluate(s"($rebuildList(rebuildList (cons 1 (cons 2 (cons 3 nil)))))"))
println(evaluate(s"($rebuildList(rebuildList (cons 1 (cons 2 (cons 3 (cons 4 nil))))))"))