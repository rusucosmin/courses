object Main {
  val msg = "Hello, world!"

  def main(args: Array[String]): Unit = {
    println(msg)
  }

  class Package[+E] {
    def contains(el: E): Boolean = true
    def getList(): Package[E]
    def head(): E
  }

  class Writer[-E] {
    def contains(el: E): Boolean = true
    def insert(): E
    def getCeva(el: E): Writer[E]
  }
}
