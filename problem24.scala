
def factorial(n: Int) = (1 to n).foldLeft(BigInt(1))( _ * _ ) 

val million = 1000000

def factoradic(n: Int) = {

  def iter(n: Int, count: Int, result: List[Int]): List[Int] = {
    //println("f() n: " + n + ", count: " + count + ", result: " + result.mkString)
    if (n == 0) result
    else {
      iter(n / count, count+1, n % count :: result)
    }
  }

  iter(n, 2, List())
}

def foo(factoradic: List[Int], alphabet: List[Int]): List[Int] = {

  def iter(factors: List[Int], alphabet: List[Int], result: List[Int]): List[Int] = {
    println("factors: " + factors.mkString + ", alphabet: " + alphabet.mkString + ", Result: " + result.mkString)

    if (factors.isEmpty) alphabet(0) :: result
    else {
      val c = alphabet(factors.head)
      iter(factors.tail, alphabet.filterNot(_ == c), c :: result)
    }
  }

  iter(factoradic, alphabet, List())
}

println("0: " + foo(factoradic(0), List(0,1,2)).mkString)
println("1: " + foo(factoradic(1), List(0,1,2)).mkString)
println("2: " + foo(factoradic(2), List(0,1,2)).mkString)
println("3: " + foo(factoradic(3), List(0,1,2)).mkString)
println("4: " + foo(factoradic(4), List(0,1,2)).mkString)
println("5: " + foo(factoradic(5), List(0,1,2)).mkString)

println("-----------")

println("101: " + factoradic(101))

val n101 = 4*factorial(4) + 
        0*factorial(3) +
        2*factorial(2) + 
        1

println("n101: " + n101)

println("Million: " + factoradic(million))

println("foo: " + foo(factoradic(million), (0 to 9).toList).reverse.mkString)

// 2783915604

val n = 2*factorial(10) +
        7*factorial(9) +
        8*factorial(8) +
        3*factorial(7) +
        9*factorial(6) +
        1*factorial(5) +
        5*factorial(4) +
        6*factorial(3) +
        0*factorial(2) + 
        4*factorial(1)

println("n: " + n)



