import sys
from utils import timing

@timing
def sum1(n):
    sum = 0
    for k in range(1, n):
        if k % 3 == 0 or k % 5 == 0:
            sum += k
    return sum

if __name__ == "__main__":
    trillion = 1000 * 1000 * 1000
    print("sum_1(trillion):     %d" % sum1(trillion))

