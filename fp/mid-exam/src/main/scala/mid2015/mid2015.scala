package mid2015
import scala._

object Mid2015 extends Mid2015 with App {
}

trait Mid2015 {
  def differences(ls: List[Int]): List[Int] = {
    ls match {
      case Nil => Nil
      case x :: xs => {
        val diff = differences(xs)
        diff match {
          case Nil => List(x)
          case _ => 
            x :: (diff.head - x) :: diff.tail
        }
      }
    }
  }
  def rebuildList(ls: List[Int]): List[Int] = {
    ls match {
      case Nil => Nil
      case x :: xs => xs.scan(x)(_ + _)
    }
  }

  def computeMinMax(b: TNode): (Int, Int) = {
    def _computeMinMax(b: Tree): (Int, Int) = {
      if (b == Leaf) (Int.MaxValue, Int.MinValue)
      else
        b match {
          case x: TNode =>  {
            val leftMinMax = _computeMinMax(x.left)
            val rightMinMax = _computeMinMax(x.right)
            (Math.min(x.elem, Math.min(leftMinMax._1, rightMinMax._1)), Math.max(x.elem, Math.max(leftMinMax._2, rightMinMax._2)))
          }
        }
    }
    _computeMinMax(b)
  }

  def isBST(x: Tree, min: Int, max: Int): Boolean = {
    if (x == Leaf) true
    else {
      x match {
        case TNode(left, elem, right) => 
          min <= elem && elem <= max && isBST(left, min, elem) && isBST(right, elem, max)
      }
    }
  }

  def isBinarySearchTree(b: Tree): Boolean = {
    isBST(b, Int.MinValue, Int.MaxValue)
  }
}

abstract class Tree
case class TNode(left: Tree, elem: Int, right: Tree) extends Tree
case object Leaf extends Tree
