package interpreter

// scalafix:off

object Lisp {

// Types -------------------------------------------------------

  type Data = Any

  case class Lambda(f: PartialFunction[List[Data], Data])

// Parsing and Prettyprinting -----------------------------------

  class LispTokenizer(s: String) extends Iterator[String] {

    private var i = 0

    private def isDelimiter(ch: Char) = ch <= ' ' || ch == '(' || ch == ')'

    def hasNext: Boolean = {
      while (i < s.length && s.charAt(i) <= ' ') {
        i += 1
      }
      i < s.length
    }

    def next: String =
      if (hasNext) {
        val start = i
        if (isDelimiter(s.charAt(i))) {
          i += 1
        }
        else {
          do {
            i += 1
          } while (i < s.length && !isDelimiter(s.charAt(i)))
        }
        s.substring(start, i)
      } else sys.error("premature end of input")
  }

  def string2lisp(s: String): Data = {

    val it = new LispTokenizer(s)

    def parseExpr(token: String): Data = {
      if (token == "(")
        parseList
      else if (token == ")")
        sys.error("unbalanced parentheses")
      else if (token.matches("^-?\\d+$"))
        Integer.parseInt(token)
      else
        Symbol(token)
    }

    def parseList: List[Data] = {
      val token = it.next
      if (token == ")")
        List()
      else
        parseExpr(token) :: parseList
    }
    parseExpr(it.next)
  }

  def lisp2string(x: Data): String = x match {
    case Symbol(name) =>
      name
    case xs: List[_] =>
      xs.map(lisp2string).mkString("(", " ", ")")
    case _ =>
      x.toString
  }

// Diagnostics---------------------------------------------------

  /** Set this to `true` to debug the interpreter */
  var trace: Boolean = false

  var curexp: Data = null
  var indent: Int = 0

  def evaluate(x: Data): Data = eval(x, globalEnv)

  def evaluate(s: String): Data = evaluate(string2lisp(s))

  def eval(x: Data, env: Environment): Data = {
    // Workaround https://github.com/lampepfl/dotty/issues/5544 by using a
    // non-breakable space instead of a regular space
    val nonBreakableSpace: String = "\u00a0"

    val prevexp = curexp
    curexp = x
    if (trace) {
      println((nonBreakableSpace * indent) + s"===> $x")
      indent += 1
    }
    val result = eval1(x, env)
    if (trace) {
      indent -= 1
      println((nonBreakableSpace * indent) + s"<=== $result")
    }
    curexp = prevexp
    result
  }

// Checked conversions ----------- -----------------------------------

  def asList(x: Data): List[Data] = x match {
    case xs: List[_] => xs
    case _ => sys.error(s"expected a list but input was $x")
  }

  def paramName(x: Data): String = x match {
    case Symbol(name) => name
    case _ => sys.error(s"malformed parameter: $x")
  }

// Environments -------------------------------------------------------

  abstract class Environment {
    def lookup(n: String): Data
    def extend(name: String, v: Data): Environment = {
      val enclosingEnvironment = this
      new Environment {
        def lookup(n: String): Data =
          if (n == name) v else enclosingEnvironment.lookup(n)
      }
    }
    def extendMulti(ps: List[String], vs: List[Data]): Environment = (ps, vs) match {
      case (List(), List()) =>
        this
      case (p :: ps1, arg :: args1) =>
        extend(p, arg).extendMulti(ps1, args1)
      case _ =>
        sys.error("wrong number of arguments")
    }
    def extendRec(name: String, expr: Environment => Data): Environment = {
      val enclosingEnvironment = this
      new Environment {
        def lookup(n: String): Data =
          if (n == name)
            expr(this)
          else
            enclosingEnvironment.lookup(n)
      }
    }
  }

  object EmptyEnvironment extends Environment {
    def lookup(n: String): Data = sys.error("undefined: " + n + ", this can happen when the wrong number of arguments is passed")
  }

  var globalEnv = EmptyEnvironment
    .extend("=", Lambda {
      case List(arg1, arg2) =>
        if (arg1 == arg2) 1 else 0
    })

    .extend("+", Lambda {
      case List(arg1: Int, arg2: Int) =>
        arg1 + arg2
    })
    .extend("-", Lambda {
      case List(arg1: Int, arg2: Int) =>
        arg1 - arg2
    })

    .extend("*", Lambda {
      case List(arg1: Int, arg2: Int) =>
        arg1 * arg2
    })
    .extend("/", Lambda {
      case List(arg1: Int, arg2: Int) =>
        arg1 / arg2
    })

    .extend("nil", Nil)
    .extend("cons", Lambda {
      case List(arg1, arg2) =>
        arg1 :: asList(arg2)
    })

    .extend("car", Lambda {
      case List(x :: xs) =>
        x
    })
    .extend("cdr", Lambda {
      case List(x :: xs) =>
        xs
    })

    .extend("null?", Lambda {
      case List(Nil) =>
        1
      case _ =>
        0
    })

// Evaluation -----------------------------------

  def eval1(x: Data, env: Environment): Data = x match {
    case _: Int =>
      x
    case Symbol(name) =>
      env.lookup(name)
    case 'val :: Symbol(name) :: expr :: rest :: Nil =>
      eval(rest, env.extend(name, eval(expr, env)))
    case 'if :: cond :: thenpart :: elsepart :: Nil =>
      if (eval(cond, env) != 0)
        eval(thenpart, env)
      else
        eval(elsepart, env)

    // syntactic sugar

    case 'and :: x :: y :: Nil =>
      eval('if :: x :: y :: 0 :: Nil, env)
    case 'or :: x :: y :: Nil =>
      eval('if :: x :: 1 :: y :: Nil, env)

    case 'case :: _ :: List('else, expr) :: Nil =>
      eval(expr, env)
    case 'case :: cond :: List(value, expr) :: rest =>
      if (eval(cond, env) == value)
        eval(expr, env)
      else
        eval('case :: cond :: rest, env)
    //  (def (name arg_1 ... arg_n) body expr)
    //  (def name (lambda (arg_1 ... arg_n) body) expr)
    case 'def :: Symbol(name) :: body :: Nil => // definition GLOBAL
      if (env == globalEnv) {
        globalEnv = env.extendRec(name, env1 => eval(body, env1))
        s"def $name" // just confirm we got the def
      }
      else {
        sys.error(s"def $name cannot be added to an inner scope because it is global.\n" +
                   "Hint: a local def always has three parameters: a name, a body, and the rest of the code to execute")
      }
    case 'def :: Symbol(name) :: body :: rest :: Nil => // GLOBAL or LOCAL
      if (env == globalEnv)
        globalEnv = env.extendRec(name, env1 => eval(body, env1))
      eval(rest, env.extendRec(name, env1 => eval(body, env1))) // evaluate
    case 'def :: prototype :: body :: expr :: Nil =>
      prototype match {
        case name :: args =>
          eval('def :: name :: List('lambda, args, body) :: expr :: Nil, env)
      }
    case 'quote :: y :: Nil =>
      y
    case 'lambda :: params :: body :: Nil =>
      mkLambda(asList(params) map paramName, body, env)
    case operator :: operands =>
      try {
        apply(eval(operator, env), operands.map(x => eval(x, env)))
      } catch {
        case ex: MatchError =>
          sys.error(s"bad arguments for function $operator: $operands")
      }
  }

  def mkLambda(ps: List[String], body: Data, env: Environment): Lambda =
    Lambda { case args =>
      eval(body, env.extendMulti(ps, args))
    }

  def apply(f: Data, args: List[Data]): Data = f match {
    case Lambda(f) =>
      f(args)
    case _ =>
      sys.error(s"application of non-function $f to arguments $args")
  }

}
