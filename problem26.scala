
lazy val ps: Stream[Int] = 2 #:: Stream.from(3).filter(i => ps.takeWhile(j => j * j <= i).forall(i % _ > 0))


val numbers = ps.takeWhile (_ < 1000).toList

//println(numbers)

def cycle(n: Int) = {
  
  def iter(n: Int, total: BigInt, log: Int): Int = {
    if (log > 2000) {
      println("Eek " + n)
      log
    }
    else if ((total -1) % n == 0) log
    else iter(n, total*10, log+1)
  }

  if (n == 2) 1
  else if (n == 5) 1
  else iter(n, 10, 1)
}

val counts = numbers.map(p => (p, cycle(p)))
val s = counts.sortWith(_._2 > _._2)
//println(counts)
println(s.head)