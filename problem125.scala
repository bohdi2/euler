
def reverse(n: Long) = {
  def iter(n: Long, r: Long): Long = {
    if (n==0) r
    else iter(n/10, r*10 + n%10)
  }

  iter(n,0)
}

def isPalindrome(n: Long) = n == reverse(n)

def sumSquares(n: Long) = n*(n+1)*(2*n+1)/6

val limit = 100000000

val answers = for (
    n <- 2 to math.sqrt(limit).toInt;
    nn = sumSquares(n);

    m <- 0 until n-1;
    mm = sumSquares(m);
    
    candidate = nn - mm;

    if (candidate) <= limit;

    if isPalindrome(candidate)
) yield candidate

//answers.foreach(println)
println(answers.toSet.size)
println(answers.toSet.sum)

