package example

import scala.annotation._

object Recitation4 {
  def deriv(expr: Expr, v: String): Expr = expr match {
    case Number(_) => Number(0)
    case Var(name) => if (name == v) Number(1) else Number(0)
    case Sum(e1, e2) => Sum(deriv(e1, v), deriv(e2, v))
    case Prod(e1, e2) => Sum(Prod(deriv(e1, v), e2), Prod(e1, deriv(e2, v)))
  }
}

abstract class Expr
case class Number(x: Int) extends Expr
case class Var(name: String) extends Expr
case class Sum(e1: Expr, e2: Expr) extends Expr
case class Prod(e1: Expr, e2: Expr) extends Expr