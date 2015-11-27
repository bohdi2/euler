package main

import "fmt"

func mod(m, n int) int {
    return ((m % n) + n) % n;
}

func gcd(a, b int) int {
    for b != 0 {
      a, b = b, a % b
    }
    return a
}

func diagonals(bounces int) int {
    return 1+(bounces+1)/2
}

func cycle(d int) int {
    return mod(-d, 3)
}

func laser(bounces int) int {
  d := diagonals(bounces)
  c := cycle(d)
  count := 0

  for ii := c; ii < d; ii += 3 {
      if gcd(d, ii) == 1 {
          count++
      }
  }

  return count
}
  
    
func main() {
    fmt.Printf("hello, world\n")

    for bounces := 1; bounces<12; bounces += 2 {
        d := diagonals(bounces)
        fmt.Printf("bounce(%d) => %d, cycle(%d) => %d, laser(%d) => %d\n",
	           bounces, d,
		   d, cycle(d),
		   bounces, laser(bounces))
    }

    const MaxUint = ^uint(0)
    fmt.Printf("%x\n", MaxUint)
    
    //b := 1000001
    var b = 1000001
    fmt.Printf("laser(%d) => %d\n", int(b), laser(int(b)))

    b = 12017639147
    fmt.Printf("laser(%d) => %d\n", int(b), laser(int(b)))
}
