/**
 * Created by chelck on 1/5/14.
 */
object Totient {

  def phi(n: Long) = {
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

}
