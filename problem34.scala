
def factorial(n: Int) = (1 to n).foldLeft(1)( _ * _ ) 

def charToDigit(c: Char) = c.toInt - 48

def charToFactorial(c: Char) = factorial(charToDigit(c))

def sumFactorials(n: Int) = n.toString().foldLeft(BigInt(0))(_ + charToFactorial(_))

def test(n: Int) = n == sumFactorials(n)

println("         9! = " + 1 * factorial(9))
println("        99! = " + 2 * factorial(9))
println("       999! = " + 3 * factorial(9))
println("      9999! = " + 4 * factorial(9))
println("     99999! = " + 5 * factorial(9))
println("    999999! = " + 6 * factorial(9))
println("   9999999! = " + 7 * factorial(9))
println("  99999999! = " + 8 * factorial(9))
println(" 999999999! = " + 9 * factorial(9))
println("9999999999! = " + 10 * factorial(9))

println("123 " + test(123))
println("145 " + test(145))

//val x = (3 to 100000).filter(test)
val x = (3 to 10000000).filter(test)

println("List " +  x + ", " + x.sum)



