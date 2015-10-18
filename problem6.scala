

def sumSquares(n: Int) = {
  (1 to n).map(i => i*i).reduceLeft(_+_)
}

def squareSums(n: Int) = {
  val s = (1 to n).reduceLeft(_+_)
  s * s
}

def diff(n: Int) = squareSums(n) - sumSquares(n)

println("Hi " + sumSquares(10))
println("Hi " + squareSums(10))
println("Hi " + diff(10))
println("Hi " + diff(100))
