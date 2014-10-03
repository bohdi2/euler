val list = for {
  n <- 1 until 1000 
  if (n % 3 == 0 || n % 5 == 0)
} yield n

println("Hi")
list.foreach(println)
println(list.reduceLeft(_+_))

