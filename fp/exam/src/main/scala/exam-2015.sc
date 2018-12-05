
// https://lamp.epfl.ch/files/content/sites/lamp/files/teaching/progfun/prev-exams/final-2015.pdf

abstract class GameAction
case object EatMushroom extends GameAction
case object JumpOnTortoise extends GameAction
case object SkidOnBanana extends GameAction
case object FallFromBridge extends GameAction


def doAction(ga: GameAction): String = ga match {
  case EatMushroom => "ate a mushroom"
  case JumpOnTortoise => "jumped on tortoise"
  case SkidOnBanana => "skid on a banana"
  case FallFromBridge => "fell from bridge"
}


val myActions: List[GameAction] = List(EatMushroom, JumpOnTortoise, SkidOnBanana)
def runGame(ls: List[GameAction]): List[String] = {
  "game starts" :: (ls map doAction)
}
runGame(myActions)

var score = 0
def doAction2(ga: GameAction): String = {
  score = ga match {
    case EatMushroom => score + 5
    case JumpOnTortoise=> score + 10
    case SkidOnBanana => score - 5
    case FallFromBridge => score - 10
  }
  doAction(ga)
}

val gameRun = "game starts" :: (myActions map doAction2)
score

final class StateM[A] (private val makeProgress: Int => (A, Int)) {
  def runState(initState: Int): (A, Int) = makeProgress(initState)

  def map[B](f: A => B): StateM[B] = {
    val res = { (s: Int) =>
      val (a, s2) = makeProgress(s)
      (f(a), s2)
    }
    new StateM(res)
  }
  def flatMap[B](f: A => StateM[B]): StateM[B] = {
    val res = { (s: Int) => 
      val (a, s2) = makeProgress(s)
      f(a).runState(s2)
    }
    new StateM(res)
  }
}





object StateM {
  def getState: StateM[Int] = new StateM((s: Int) => (s, s))
  def putState(newState: Int): StateM[Unit] = new StateM((s: Int) => ((), newState))
  def unit[A](a: A): StateM[A] = {
    new StateM[A](x => (a, x))
  }
}














def doAction3(ga: GameAction): StateM[String] = ga match {
  case EatMushroom => StateM.unit("eat mushroom")
  case JumpOnTortoise => StateM.unit("jump on tortoise")
  case SkidOnBanana => StateM.unit("skid on banana")
  case FallFromBridge => StateM.unit("fall from bridge")
}
def runGame3(ls: List[GameAction]): StateM[List[String]] =
  ls.foldLeft[StateM[List[String]]](StateM.unit(List("game starts"))) {
    case (prevState, newAction) =>
      for {
        msg <- prevState
        msg2 <- doAction3(newAction)
      } yield {
        msg ++ List(msg2)
      }
  }
runGame3(myActions).runState(0)



