object Main {
  val msg = "Hello, world!"

  def main(args: Array[String]): Unit = {
    println(msg)
    List(1, 2, 3).foldLeft(0)(_ + _)
  }
}
