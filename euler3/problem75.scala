
def gcd(a: Int, b: Int): Int = {
  if (b == 0) a
  else gcd(b, a % b)
}

def foo2(limit: Int) = {
  val mMax = math.sqrt(limit/2).toInt

  for (
    m <- 2 to mMax;
    n <- 1 until m;
    if (m+n) % 2 == 1;
    if gcd(m,n) == 1;

    a = m*m - n*n;
    b = 2 * m * n;
    c = m*m + n*n;

    if a+b+c <= limit && (limit % (a+b+c)) == 0;

    factor = limit / (a+b+c)
    
  ) yield (factor * (a + b + c))
}

val lengths = foo2(1500000).toList

println("Hi: " + lengths.size)

val xx = lengths.groupBy(x=>x)

println("Hi: " + xx.filter(p => 1 == p._2.size).size)
