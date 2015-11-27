#include <stdio.h>

int main(int argc, char **argv) {
  long trillion = 1000 * 1000 * 1000;
  
  long sum = 0;
  long ii;
  
  for (ii = 0; ii<trillion; ii++) {
    if (ii%3 == 0 || ii%5 == 0) {
      sum += ii;
    }
  }
  printf("sum = %lu\n", sum);
  return 0;
}
