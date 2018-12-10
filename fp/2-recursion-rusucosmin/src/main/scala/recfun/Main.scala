package recfun

object Main {
  def main(args: Array[String]): Unit = {
    println("Pascal's Triangle")
    for (row <- 0 to 10) {
      for (col <- 0 to row)
        print(pascal(col, row) + " ")
      println()
    }
  }

  /**
   * Exercise 1
   */
    def pascal(c: Int, r: Int): Int = {
      if (c == 0) {
        1
      } else if (c > r) {
        0
      } else {
        pascal(c - 1, r - 1) + pascal(c, r - 1)
      }
    }
  
  /**
   * Exercise 2
   */
    def balance(chars: List[Char]): Boolean = {
      def _balance(chars: List[Char], openedSoFar: Int): Boolean = {
        chars match {
          case Nil => if (openedSoFar == 0) true else false
          case x::tail =>
            x match {
              case '(' => _balance(tail, openedSoFar + 1)
              case ')' =>
                if (openedSoFar == 0) false
                else _balance(tail, openedSoFar - 1)
              case _ => _balance(tail, openedSoFar)
            }
        }
      }
      _balance(chars, 0)
    }
  
  /**
   * Exercise 3
   */
    def countChange(money: Int, coins: List[Int]): Int = {
      money match {
        // assuming real life coins value always > 0, no way we can sum 0
        case 0 => 0
        // if negative, no way
        case x if x < 0 => 0
        // if greater > 0 => which is the only left case
        case x =>
          // check what coins we have left
          coins match {
            // no coins => cannot pay anything
            case Nil => 0
            // at least one coin
            case x::tail =>
              // if it has the same values as the current coin, count 1
              // and add how many we can create using the remaining coins
              // otherwise, use the current coint or not use it
              if(x == money) {
                1 + countChange(money,  tail)
              } else {
                countChange(money, tail) + countChange(money - x, coins)
              }
          }
      }
    }
  }
