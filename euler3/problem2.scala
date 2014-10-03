 


lazy val fib: Stream[Int] = Stream.cons(0, Stream.cons(1, fib.zip(fib.tail).map(p => p._1 + p._2)))

val result = fib.filter(_ % 2 == 0).takeWhile(_ < 4000000).reduceLeft(_+_)

println("Answer: " + result)
