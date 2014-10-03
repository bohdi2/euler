
def reverse(n: BigInt) = {
  def iter(n: BigInt, r: BigInt): BigInt = {
    if (n==0) r
    else iter(n/10, r*10 + n%10)
  }

  iter(n,0)
}

def isPalindrome(n: BigInt) = n == reverse(n)

def lychrel(n: Int) = {
  val limit = 60

  //println("lychrel: " + n)
  def iter(n: BigInt, count: Int): Int = {
      //println("iter: " + n + ", " + count)
      if (count == limit) count
      else {
        val next = n + reverse(n)
        //println("next: " + next);
        if (isPalindrome(next)) count+1
        else iter(next, count+1)
    }
  }
  iter(BigInt(n),0)
}
  

val domain = (1 until 10000).map(lychrel).filter(_>50)

println(domain.size)





