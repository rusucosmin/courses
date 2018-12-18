

def derive(x: Symbol, expr: Any): Any = expr match {
  case Symbol("+") :: f :: g :: Nil =>
      Symbol("+") :: derive(x, f) :: derive(x, g) :: Nil
  case Symbol("*") :: f :: g :: Nil =>
      Symbol("*") :: List(Symbol("*"), derive(x, f), g)::
      List(Symbol("*"), f, derive(x, g)) :: Nil
  case y: Symbol => if (x == y) 1 else 0
  case n: Int => return 0
}


derive('x, List('+, 'y, List('+, 2, 'x)))
derive('x, 'x)
derive('x, 'y)
derive('x, 10)
derive('x, List('+, 'x, 'y))
derive('x, List('*, 'x, 'y))


def testStartsWith(input: Stream[Char], pattern: List[Char]): Option[Stream[Char]] = 
  if (input.take(pattern.length) == pattern)
    Some(input.drop(pattern.length))
  else
    None

assert(testStartsWith(Stream('a', 'b', 'c'), List('a', 'b')) == Some(Stream('c')))
assert(testStartsWith(Stream('a', 'b', 'c'), List('b', 'c')) == None)
assert(testStartsWith('a' #:: 'b' #::
  Stream.from(1).map(x => (x % 255).toChar).take(10), List('a')) ==
  Some('b' #:: Stream.from(1).map(x => (x % 255).toChar).take(10)))

def replaceAll(input: Stream[Char], pattern: List[Char],
  replacement: List[Char]): Stream[Char] = testStartsWith(input, pattern) match {
    case Some(nxt) => replaceAll(replacement.toStream #::: nxt, pattern, replacement)
    case None => input match {
      case Stream.Empty => Stream.Empty
      case head #:: tail => head #:: replaceAll(tail, pattern, replacement)
    }
  }

assert(replaceAll(Stream('a', 'a', 'a'), List('a', 'a'), List('b')) == Stream('b', 'a'))
assert(replaceAll(Stream('a', 'a', 'b', 'a', 'b', 'a'),List('a', 'b', 'a'), List('b', 'a')) ==
    Stream('a', 'b', 'b', 'a'))

def replaceAllMany(input: Stream[Char],
  patternsAndReplacements: List[(List[Char], List[Char])]): Stream[Char] = {
    val valid = patternsAndReplacements.filter{case (pattern, replacement) => !testStartsWith(input, pattern).isEmpty}
    valid match {
      case Nil => input match {
        case Stream.Empty => Stream.Empty
        case head #:: tail => head #:: replaceAllMany(tail, patternsAndReplacements)
      }
      case (pattern, replacement) :: _ => {
        testStartsWith(input, pattern) match {
          case Some(nxt) => replaceAllMany(replacement.toStream #::: nxt, patternsAndReplacements)
        }
      }
    }
  }

assert(replaceAllMany(Stream('a', 'a', 'b', 'b'), List((List('a', 'b'), List('c')), (List('a', 'a'), List('d'))))
== Stream('d', 'b', 'b'))

assert(replaceAllMany(Stream('d', 'a', 'a', 'a', 'b', 'b'), List(
  (List('e', 'b'), List('c')),
  (List('a', 'a', 'a'), List('d', 'e')),
  (List('d', 'd'), List('z')))) == Stream('d', 'd', 'c', 'b'))