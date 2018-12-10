package quickcheck

import common._

import org.scalacheck._
import Arbitrary._
import Gen._
import Prop._

abstract class QuickCheckHeap extends Properties("Heap") with IntHeap {

  lazy val genHeap: Gen[H] = oneOf(
    const(empty),
    for {
      elem <- arbitrary[Int]
      h <- oneOf(const(empty), genHeap)
    } yield insert(elem, h)
  )
  implicit lazy val arbHeap: Arbitrary[H] = Arbitrary(genHeap)

  property("gen1") = forAll { (h: H) =>
    val m = if (isEmpty(h)) 0 else findMin(h)
    findMin(insert(m, h)) == m
  }

  /*If you insert any two elements into an empty heap, finding the minimum of the resulting heap should get the smallest of the two elements back.*/
  property("min2") = forAll { (x: Int, y: Int) => {
    (insert(x, insert(y, empty)) == Math.min(x, y))
  }}

  /*If you insert an element into an empty heap, then delete the minimum, the resulting heap should be empty.*/
  property("insert1delete1") = forAll { (x: Int) => {
    deleteMin(insert(x, empty)) == empty
  }}

  /*Given any heap, you should get a sorted sequence of elements when continually finding and deleting minima. (Hint: recursion and helper functions are your friends.)*/
  property("findMinDeleteMinShouldYieldSortedArray") = forAll{ (h: H) => {
    def toSortedList(h: H): List[Int] =
      if (isEmpty(h)) Nil
      else
        findMin(h) :: toSortedList(deleteMin(h))
    toSortedList(h) == toSortedList(h).sorted
  }}

  /*Finding a minimum of the melding of any two heaps should return a minimum of one or the other.*/
  property("melt2Heaps2Min") = forAll { (h1: H, h2: H) =>
    findMin(meld(h1, h2)) == Math.min(findMin(h1), findMin(h2))
  }
}
