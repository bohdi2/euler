/**
 * Created by chelck on 1/5/14.
 */


object Euler {


  def main(args: Array[String]) = {
    val problems = Map(214 -> Problem214,
                       999 -> Problem999)

    val n = 214

    problems.get(n) match {
      case Some(p) => {
        val actual = p()
        if (actual != p.expected)
          println(s"Problem${n} expected ${p.expected}, but calculated $actual")
        else
          println("ok")
       }
      case _ => println("214 not found")
    }
  }

}
