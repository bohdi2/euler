
  def phi(n: Int) = {
    var nn = n
    var tot = n

    var p = 2

    while (p * p <= nn) {
      if (nn % p == 0) {
        // p divides nn
        tot = tot / p
        tot = tot * (p - 1)

        while (nn % p == 0)
          nn = nn / p
      }
      p = p + 1
    }

    if (nn > 1) {
      tot = tot / nn
      tot *= (nn - 1)
    }
    tot
  }

  //def N(start: Long, end: Long, step: Long) = (start to end by step).map(phi).sum
  //def S(m: Long, start: Long, end: Long, step: Long) = (start to end by step).map(k => phi(k*m)).sum

  def x(k: Int, n: Int, c: Int) = println(n, k, phi(k)*phi(n), phi(k*n), c)

  println("phi(2) = " + phi(2))
  println("phi(3) = " + phi(3))
  println("phi(6) = " + phi(6))

  x(6,7, 0)
  x(6,8, phi(6)*phi(8)*2/phi(2))
  x(6,9, phi(6)*phi(9)*3/phi(3))
  x(6,10, phi(6)*phi(10)*2/phi(2))
  x(6,11, 0)
  x(6,12, phi(6)*phi(12)*3/phi(3)*2/phi(2))
  x(6,13, 0)
  x(6,14, phi(6)*phi(14)*2/phi(2))
  x(6,15, phi(6)*phi(15)*3/phi(3))
  x(6,360, phi(6)*phi(360)*3/phi(3)*2/phi(2))



