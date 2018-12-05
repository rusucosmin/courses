case class Movie(title: String, director: String, releaseDate: Int, leadActors: List[String])

val movies: List[Movie] = List(
  Movie("The Master", "Paul Thomas Anderson", 2012,
    List("Joaquin Phoenix", "Philip Seymour Hoffman", "Amy Adams")
  ),
  Movie("Unforgiven", "Clint Eastwood", 1992,
    List("Clint Eastwood", "Gene Hackman", "Morgan Freeman")
  ),
  Movie("Magnolia", "Paul Thomas Anderson", 1999,
    List("Tom Cruise", "Philip Seymour Hoffman", "William H. Macy")
  ),
  Movie("The Big Lebowski", "Joel and Ethan Coen", 1998,
    List("Jeff Bridges", "John Goodman", "Philip Seymour Hoffman")
  ),
  Movie("Million Dollar Baby", "Clint Eastwood", 2004,
    List("Clint Eastwood", "Hilary Swank", "Morgan Freeman")
  ),
  Movie("The Grand Budapest Hotel", "Wes Anderson", 2014,
    List("Ralph Fiennes", "F. Murray Abraham", "Mathieu Amalric")
  ),
  Movie("The Good, the Bad and the Ugly", "Sergio Leone", 1966,
    List("Clint Eastwood", "Eli Wallach", "Lee Van Cleef")
  )
)

for {
  movie <- movies
} yield {
  s"${movie.title}, directed by ${movie.director} (${2014 - movie.releaseDate} years ago)"
}

movies map {(movie) => s"${movie.title}, directed by ${movie.director} (${2014 - movie.releaseDate} years ago)"}

for {
  movie <- movies
  actor <- movie.leadActors
  if actor == "Philip Seymour Hoffman"
} yield movie.title

movies flatMap {
  movie =>
    movie.leadActors.withFilter{actor =>
      actor == "Philip Seymour Hoffman"
    }.map{_ =>
      movie.title
    }
}

for {
  movie <- movies
  director = movie.director
  actor <- movie.leadActors
  if (director == actor)
} yield {
  (director, movie.title)
}

movies.foldLeft[Map[String, List[String]]](Map[String, List[String]]()){
  case (prevMap, movie) =>
    if (movie.leadActors contains movie.director)
      prevMap get movie.director match {
        case None => prevMap ++ Map(movie.director -> List(movie.title))
        case Some(x) => {
          val nxtList =
            if (x contains movie.title) x
            else movie.title :: x
          prevMap ++ Map(movie.director -> nxtList)
        }
      }
    else prevMap
}


abstract class Formula
final case class Var(name: String) extends Formula
final case class Not(p: Formula) extends Formula
final case class And(p: Formula, q: Formula) extends Formula
final case class Or(p: Formula, q: Formula) extends Formula
final case class Implies(p: Formula, q: Formula) extends Formula

def elimImplies(f: Formula): Formula = f match {
  case x: Var => x
  case Not(p) => Not(elimImplies(p))
  case And(p, q) => And(elimImplies(p), elimImplies(q))
  case Or(p, q) => Or(elimImplies(p), elimImplies(q))
  case Implies(p, q) => Or(Not(elimImplies(p)), elimImplies(q))
}

def negationNormalForm(f: Formula): Formula = f match {
  case x: Var => x
  case Not(x) => {
    x match {
      case v: Var => f
      case Not(p) => negationNormalForm(p)
      case And(p, q) => Or(negationNormalForm(Not(p)), negationNormalForm(Not(q)))
      case Or(p, q) => And(negationNormalForm(Not(p)), negationNormalForm(Not(q)))
    }
  }
  case And(p, q) => And(negationNormalForm(p), negationNormalForm(q))
  case Or(p, q) => Or(negationNormalForm(p), negationNormalForm(q))
}

def checkRow(row: Array[Boolean]): Boolean = {
  row.count((x) => x) == 1
}

checkRow(Array(true, true, false))
checkRow(Array(false, true, false))
checkRow(Array(false, false, false))

def checkPositioning(board: Array[Array[Boolean]]): Boolean = {
  val rowChecks = for {
    line <- board
  } yield checkRow(line)
  val rowsValid = rowChecks.count((x) => !x) == 0
  val colChecks = for {
    line <- board.transpose
  } yield checkRow(line)
  val colValid = rowChecks.count((x) => !x) == 0
  rowsValid && colValid
}

val handWrittenFormula: Formula =
  Or(
    And(
      Var("1"),
      And(
        Not(Var("2")),
        Not(Var("3")))),
    Or(
      And(
        Not(Var("1")),
        And(
          Var("2"),
          Not(Var("3")))),
      And(
        Not(Var("1")),
        And(
          Not(Var("2")),
          Var("3"))),
    )
  )

  def formulaForRow(row: Array[Var]): Formula = {
    val n = row.count((_) => true)
    val orS = for {
      i <- 1 to n
    } yield {
      val notVars = for {
        j <- 1 to n
        if i != j
      } yield {
        Not(row(j))
      }
      notVars.foldLeft[Formula](row(i))(And(_, _))
    }
    orS.reduce(Or(_, _))
  }






