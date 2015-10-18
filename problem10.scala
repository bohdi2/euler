
lazy val ps: Stream[Int] = 2 #:: Stream.from(3).filter(i => ps.takeWhile(j => j * j <= i).forall(i % _ > 0))

println(ps.takeWhile(_ < 2000000).foldLeft(0L)(_+_))

