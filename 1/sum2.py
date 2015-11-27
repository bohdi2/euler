import sys
from utils import timing

@timing
def sum2(n):
    return S(n, 3) + S(n, 5) - S(n, 15)

def S(n, d):
    return d * t((n - 1) // d)

def t(n):
    return n * (n + 1) // 2

if __name__ == "__main__":
    billion = 1000 * 1000
    trillion = 1000 * 1000 * 1000
    print("sum2(10):       %d" % sum2(10))
    print("sum2(billion):  %d" % sum2(billion))
    print("sum2(trillion): %d" % sum2(trillion))
