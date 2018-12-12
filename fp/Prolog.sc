/* 
A simple Prolog interpreter.
Instead of a parser, this time we embed the language into Scala.
See object Test {...} at the end of this file for examples on
invoking the language within Scala.

Example use:

scalac Prolog.scala
scala -cp . Test 

  ===>

ancestor('fred, 'peter)?
yes
ancestor('mary, 'peter)?
yes
ancestor('john, 'peter)?
yes
ancestor('paul, 'peter)?
no
ancestor('X, 'peter)?
['X = 'peter]
more
['X = 'john]
more
['X = 'mary]
more
['X = 'fred]
more
no
yes
no
['X = 'paul]
*/
object Prolog {
  import scala.language.postfixOps
  import scala.language.implicitConversions
  import Iterator.{empty, single}

  var showMatches = false
  var trace = false

// --- Terms ----------------------------------------------

  abstract class Term
  {
    def subst(s: Subst): Term
    def apply(ts: Term*): Constructor = sys.error("" + this + " cannot be applied")
    def :: (t: Term) = new ListConstructor(t, this)
  }

  case class Variable(name: String) extends Term
  {
    assert(Character.isUpperCase(name.charAt(0)), name)
    def subst(s: Subst): Term = lookup(s, name) match {
      case Some(t) => t subst s
      case None => this
    }
    override def toString(): String = "'" + name
  }

  case class Constructor(name: String, ts: List[Term]) extends Term
  {
    def subst(s: Subst): Term = Constructor(name, ts map (_.subst(s)))
    override def toString(): String = "'" + name + ts.mkString("(", ",", ")")
  }

  class ListConstructor(hd: Term, tl: Term) extends Constructor("::", List(hd, tl))
  {
    override def subst(s: Subst): Term = new ListConstructor(hd subst s, tl subst s)
    override def toString(): String = hd.toString() + " :: " + tl.toString()
  }

  class Constant(name: String) extends Constructor(name, List())
  {
    assert(!Character.isUpperCase(name.charAt(0)), name)
    override def subst(s: Subst): Term = this
    override def apply(ts: Term*): Constructor = new Constructor(name, ts.toList)
    override def toString(): String = "'" + name
  }

  implicit def symbol2term(s: Symbol): Term =
    if (Character.isUpperCase(s.name.charAt(0))) Variable(s.name)
    else new Constant(s.name)

  implicit def int2constant(n: Int): Constant =
    new Constant(n.toString) {
      override def toString = n.toString
    }

  def freeVars(t: Any): List[String] = t match {
    case Variable(name) => List(name)
    case Constructor(name, ts) => freeVars(ts)
    case And(q1, q2) => freeVars(List(q1, q2))
    case Apply(p, args) => freeVars(args)
    case Clause(hd, tl) => freeVars(List(hd, tl))
    case ts: List[_] => (ts flatMap freeVars).distinct
    case _ => List()
  }

  private var count = 0
  def newVar(prefix: String): Variable = {
    count = count + 1
    Variable(prefix + count)
  }

// --- Substitutions ----------------------------------------

  case class Binding(name: String, term: Term) {
    term match {
      case Variable(n) if (name == n) => sys.error("bad binding")
      case _ =>
    }
    override def toString() = "'" + name + " = " + term
  }

  type Subst = List[Binding]

  def lookup(s: Subst, name: String): Option[Term] = s match {
    case List() => None
    case b :: s1 => if (name == b.name) Some(b.term) else lookup(s1, name)
  }

  def rename(s: String) = Binding(s, newVar(s))


// --- Unification ------------------------------------------

  def unify(x: Term, y: Term, s: Subst): Iterator[Subst] = {
    val result = (x, y) match {
      case (Variable(a), Variable(b)) if (a == b) =>
        single(s)
      case (Variable(a), _) => lookup(s, a) match {
        case Some(x1) => unify(x1, y, s)
        case None => if (freeVars(y) contains a) empty else single(Binding(a, y) :: s)
      }
      case (_, Variable(b)) => lookup(s, b) match {
        case Some(y1) => unify(x, y1, s)
        case None => if (freeVars(x) contains b) empty else single(Binding(b, x) :: s)
      }
      case (Constructor(a, ts), Constructor(b, us)) if (a == b) =>
        unify(ts, us, s)
      case (x, y) =>
        if (x != y) empty else single(s)
    }
    if (showMatches) Console.println("unify " + x + " with " + y + " = " + result.hasNext)
    result
  }

  def unify(xs: List[Term], ys: List[Term], s: Subst): Iterator[Subst] = (xs, ys) match {
    case (List(), List()) =>
      single(s)
    case (x :: xs1, y :: ys1) =>
      for {
        s1 <- unify(x, y, s)
        s2 <- unify(xs1, ys1, s1)
      } yield s2
    case _ =>
      empty
  }

// --- Solutions ------------------------------------------

  var currentSolutions: Iterator[Subst] = empty
  var currentFreeVars: List[String] = List()

  def more: String = {
    val r = nextSolution(currentSolutions, currentFreeVars contains)
//    System.out.println(r)
    r
  }

  def nextSolution(solns: Iterator[Subst], p: String => Boolean): String =
    if (solns.hasNext) {
      val s = solns.next
      val proj =
        for (Binding(a, t) <- s if p(a))
        yield "'" + a + " = " + t.subst(s)
      if (proj.isEmpty) "yes" else proj.mkString("[", ", ", "]")
    } else "no"

// --- Constraints ------------------------------------------

  abstract class Query {
    def subst(s: Subst): Query
    def solve(s: Subst): Iterator[Subst]
    def solve1(s: Subst): Iterator[Subst] =
      if (trace) {
        val (ss1, ss2) = solve(s).duplicate
        System.out.println("solved " + this + " at " + s + " = " + nextSolution(ss1, s => true))
        ss2
      } else solve(s)
    def & (q: Query): Query = And(this, q)
    def ? : String = {
      currentFreeVars = freeVars(this)
      currentSolutions = solve(List())
      more
    }
    def ?[T](x: => T): T = { this?; x }
  }

  case object True extends Query {
    def subst(s: Subst): Query = this
    def solve(s: Subst): Iterator[Subst] = single(s)
  }

  case class And(q1: Query, q2: Query) extends Query {
    def subst(s: Subst): Query = And(q1 subst s, q2 subst s)
    def solve(s: Subst): Iterator[Subst] =
      for (s1 <- q1 solve1 s; s2 <- q2 solve1 s1) yield s2
  }

  case class not(q: Query) extends Query {
    def subst(s: Subst): Query = not(q subst s)
    def solve(s: Subst): Iterator[Subst] = {
      val s1 = q.solve(s)
      if (s1.hasNext) empty else single(s)
    }
  }

  case class Apply(p: Predicate, arguments: List[Term]) extends Query {
    def subst(s: Subst): Apply = Apply(p, arguments map (_.subst(s)))
    def solve(s: Subst): Iterator[Subst] =
      for {
        clause <- p.clauses map (_.newInstance)
        s1 <- unify(clause.hd.arguments, arguments, s)
        s2 <- clause.tl solve1 s1
      } yield s2
    def :- (q: Query): Predicate = p.addClause(this, q)
    def ! : Unit = p.addClause(this, True)
    def ![T](x: => T): T = { this!; x }
  }

// --- Predicates --------------------------------------------

  case class Clause(hd: Apply, tl: Query) {
    def newInstance: Clause = {
      val s = freeVars(this) map rename
      Clause(hd subst s, tl subst s)
    }
  }

  private class Linked[T] { var elem: T = _; var next: Linked[T] = _}

  class Predicate {
    private var initClauseRef = new Linked[Clause]
    private var lastClauseRef = initClauseRef

    def addClause(hd: Apply, tl: Query) = {
      lastClauseRef.next = new Linked
      lastClauseRef.next.elem = Clause(hd, tl)
      lastClauseRef = lastClauseRef.next
      this
    }

    def & (q: Query): Predicate = {
      lastClauseRef.elem = Clause(lastClauseRef.elem.hd, lastClauseRef.elem.tl & q)
      this
    }

    def clauses = new Iterator[Clause] {
      private var current = initClauseRef
      def hasNext = current != lastClauseRef
      def next = { current = current.next; current.elem }
    }

    def apply(ts: Term*): Apply = Apply(this, ts.toList)
  }
}
import Prolog._
import scala.language.postfixOps

  val append = new Predicate

  // We use Symbol for Prolog variables and constants.
  // For lists, we use Scala lists instead of Prolog syntax
  // :- is an operator that also adds clause to database
  append('X :: 'Xs, 'Ys, 'X :: 'Zs) :- append('Xs, 'Ys, 'Zs)   
  // For facts/axioms that have no :-, we use ! at the end.
  append('nil, 'Xs, 'Xs)!
  // We do not use "." at the end of clauses.

  // These 'println' are to help you make sense of console output
  println("append('one :: 'nil, 'two :: 'nil, 'X)?")
  println(append('one :: 'nil, 'two :: 'nil, 'X)?)

  append('one :: 'nil, 'X, 'one :: 'two :: 'nil)?
  append('X, 'two :: 'nil, 'one :: 'two :: 'nil)?

  println("append('one :: 'nil, 'X, 'Y)?")
  println(append('one :: 'nil, 'X, 'Y)?)

  println("append('one :: 'nil, 'X, 'X)?")
  println(append('one :: 'nil, 'X, 'X)?)


  val parent = new Predicate
  parent('john, 'mary)! parent('john, 'paul)! 
  parent('mary, 'fred)! parent('fred, 'peter)!

  val ancestor = new Predicate
  ancestor('X, 'X)
  // We use '&' instead of ',' of Prolog
  ancestor('X, 'Z) :- parent('X, 'Y) & ancestor('Y, 'Z)

  println("ancestor('fred, 'peter)?")
  println(ancestor('fred, 'peter)?)
  println("ancestor('mary, 'peter)?")
  println(ancestor('mary, 'peter)?)
  println("ancestor('john, 'peter)?")
  println(ancestor('john, 'peter)?)
  println("ancestor('paul, 'peter)?")
  println(ancestor('paul, 'peter)?)
  println("ancestor('X, 'peter)?")
  println(ancestor('X, 'peter)?)
  // 'more' is like typing ';' on Prolog prompt
  println("more")
  println(more)
  println("more")
  println(more)
  println("more")
  println(more)
  println("more")
  println(more)

  val same = new Predicate
  same('X, 'X)!

  val sibling = new Predicate;
  sibling('X, 'Y) :- parent('Z, 'X) & parent('Z, 'Y) & not(same('X, 'Y))

  println("Siblings")
  println(sibling('mary, 'paul)?)
  println(sibling('mary, 'mary)?)
  println(sibling('mary, 'X)?)
  println(more)
