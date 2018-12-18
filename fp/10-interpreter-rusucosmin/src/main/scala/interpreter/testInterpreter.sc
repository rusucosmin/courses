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

val lispEx2 = """
  (def (derive x expr) expr (derive (cons (quote x) (cons (quote +) (cons (quote y) (cons (quote +) 2 (quote x)))))))
"""

println(evaluate(lispEx2))

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