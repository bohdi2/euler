
lazy val ps: Stream[Int] = 2 #:: Stream.from(3).filter(i => ps.takeWhile(j => j * j <= i).forall(i % _ > 0))

val n=600851475143L
val limit = math.sqrt(n)


def foo(n: Long, result: Long, primes: Stream[Int]): Long = {
  if (n == 1) result
  else {
    val p = primes(0)
    if (n % p == 0) foo(n/p, math.max(result, p), primes)
    else foo(n, result, primes.tail)
  }
}

println(foo(n, 1, ps))
