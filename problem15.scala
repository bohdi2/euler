
implicit def pimp(n:Int) = new { def ! = (1 to n).foldLeft(BigInt(1))( _ * _ ) }

println("6! " + (6!))
println("20! " + (20!))

val n = 20!

println( (40!) / (n * n))

