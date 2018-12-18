/*
1) Write a stream of squares of integers ≥ 1. You may use Stream.from(i: Int)
*/

val squares: Stream[Int] = Stream.from(1).map(x => x * x)

/*
2) Write a stream of all non-empty strings using the characters "0" and "1" and the
concatenation operation +. In other words, every non-empty string composed of "0" and "1"
should be reached at some point.
*/

val codes: Stream[String]  = "0" #:: "1" #:: codes.flatMap(x => Stream(x + "0", x + "1"))

codes.take(10).toList

/*
3) Using codes, write a stream of all possible non-empty palindromes of “0” and “1”. You
may use the .reverse function defined on strings.
*/

val palCode = codes filter (x => x.reverse == x)

palCode.take(10).toList

/*
4) Can you do the same without filtering? The palindromes need not to be in the same order.
*/

val palCode2 = "0" #:: "1" #:: (codes flatMap (x => Stream(x + x.reverse, x + "0" + x.reverse, x + "1" + x.reverse)))

palCode2.take(10).toList

/*

5) Given another stream otherCodes, possibly finite or infinite, you don’t know at first:
val otherCodes: Stream[String] = [some external source]
can you build a stream allCodes interleaving palCodes and otherCodes ?
*/

val otherStream = Stream("ana", "are", "mere")

def interleaveAux(palCode: Stream[String], otherStream: Stream[String]): Stream[(String, String)] =
  (palCode, otherStream) match {
    case (Stream.Empty, _) => Stream.Empty
    case (_, Stream.Empty) => Stream.Empty
    case (x #:: xs, y #:: ys) => (x, y) #:: interleaveAux(xs, ys)
  }

val interleave = interleaveAux(palCode, otherStream)

interleave take(10) toList

def interleave2Aux(palCode: Stream[String], otherStream: Stream[String]): Stream[String] =
  (palCode, otherStream) match {
    case (Stream.Empty, xs) => xs
    case (xs, Stream.Empty) => xs
    case (x #:: xs, y #:: ys) => x #:: y #:: interleave2Aux(xs, ys)
  }

val interleave2 = interleave2Aux(palCode, otherStream)

interleave2 take(10) toList

val x = Stream.from(1).map((x) => {println(s"compute$x"); x})

x.take(2).toList