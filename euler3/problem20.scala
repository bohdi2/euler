
def factorial(n: Int) = (1 to n).foldLeft(BigInt(1))( _ * _ ) 

def charToDigit(c: Char) = c.toInt - 48
def sumDigits(s: String) = s.foldLeft(0)(_ + charToDigit(_))

val s = factorial(100).toString

println("100! = " + s)

println("Sum of the digits of 100! is " + sumDigits(s))



