
def test(n: Int, divisor: Int): Boolean = {
    if (divisor == 1) true
    else (n % divisor) == 0 && test(n, divisor - 1)
}

val x = (1 to 1000000000).filter(test(_, 20))

System.out.println(x)
