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

    
func count(d, c int) int {
  count := 0

  for ii := c; ii < d; ii += 3 {
      if gcd(d, ii) == 1 {
          count++
      }
  }

  return count
}
  
func laser(bounces int) int {
  d := diagonals(bounces)
  c := cycle(d)
  return count(d, c)
}
  
    
func main() {
    
    var b = 1000001
    fmt.Printf("laser(%d) => %d\n", int(b), laser(int(b)))

    b = 12017639147
    fmt.Printf("laser(%d) => %d\n", int(b), laser(int(b)))
}
