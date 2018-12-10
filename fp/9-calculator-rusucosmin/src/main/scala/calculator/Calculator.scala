package calculator

sealed abstract class Expr
final case class Literal(v: Double) extends Expr
final case class Ref(name: String) extends Expr
final case class Plus(a: Expr, b: Expr) extends Expr
final case class Minus(a: Expr, b: Expr) extends Expr
final case class Times(a: Expr, b: Expr) extends Expr
final case class Divide(a: Expr, b: Expr) extends Expr

object Calculator extends CalculatorInterface {
  def computeValues(
      namedExpressions: Map[String, Signal[Expr]]): Map[String, Signal[Double]] = {
        namedExpressions mapValues {(sigExpr) => Var({
          eval(sigExpr(), namedExpressions)
        })}
  }

  def _eval(expr: Expr, references: Map[String, Signal[Expr]], refs: Set[String]): Double = {
    expr match {
      case Literal(v) => v
      case Ref(name) => {
        if (references contains name)
          if (refs contains name)
            Double.NaN
          else
            _eval(references(name)(), references, refs + name)
        else
          Double.NaN
      }
      case Plus(a, b) => _eval(a, references, refs) + _eval(b, references, refs)
      case Minus(a, b) => _eval(a, references, refs) - _eval(b, references, refs)
      case Times(a, b) => _eval(a, references, refs) * _eval(b, references, refs)
      case Divide(a, b) => {
        val valB = _eval(b, references, refs)
        if (valB == 0)
          Double.NaN
        else
          _eval(a, references, refs) / valB
      }
    }
  }

  def eval(expr: Expr, references: Map[String, Signal[Expr]]): Double = {
    _eval(expr, references, Set())
    /*
    expr match {
      case Literal(v) => v
      case Ref(name) => {
        if (references contains name)
          eval(references(name)(), references)
        else
          Double.NaN
      }
      case Plus(a, b) => eval(a, references) + eval(b, references)
      case Minus(a, b) => eval(a, references) - eval(b, references)
      case Times(a, b) => eval(a, references) * eval(b, references)
      case Divide(a, b) => {
        val valB = eval(b, references)
        if (valB == 0)
          Double.NaN
        else
          eval(a, references) / valB
      }
    }*/
  }

  /** Get the Expr for a referenced variables.
   *  If the variable is not known, returns a literal NaN.
   */
  private def getReferenceExpr(name: String,
      references: Map[String, Signal[Expr]]) = {
    references.get(name).fold[Expr] {
      Literal(Double.NaN)
    } { exprSignal =>
      exprSignal()
    }
  }
}
