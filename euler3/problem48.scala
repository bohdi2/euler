
	
def self(n: Int) = List.fill(n)(BigInt(n)).product

val result = (1 to 1000).map(self).sum
println(result)
    