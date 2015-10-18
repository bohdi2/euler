
def isPalindrome(n: Int) = {
  val s = n.toString
  s == s.reverse
}

val palindromes = for (
  a <- 1 to 999;
  b <- 1 to 999;
  if isPalindrome(a*b)
) yield a*b

println("Palidromes: " + palindromes.max)
