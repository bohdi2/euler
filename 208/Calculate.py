#!/usr/bin/env python3

import collections
import itertools
from math import factorial
import sys


def choose(n, k):
    return factorial(n) // (factorial(k) * factorial(n-k))


def all_choices(n, step):
    return sum([choose(n, k) for k in range(0, n+1, step)])


def main(args):
    f = factorial
    length = 25
    print("all:", all_choices(length, 5))
    print("2**25:", 2**length)
    print(choose(length, 2))

    print(24, 3099626)
    print(22, 2669305)

    print("pre", choose(23, 0) + choose(23, 5) + choose(23,10) + choose(23, 15) + choose(23, 20))
    print("pr2", all_choices(25, 5))
    print("pr2", f(25) // (f(5)**5))

    count = 0
    for p in itertools.product("12345", repeat=length):
        c = collections.Counter(p)
        if c['R'] % 5 == 0:
            count += 1

    print("count", count)

    # 22
    #for p in itertools.product("12345", repeat=length):
    #    print("".join(p))

    #print(choose(10,5))
    #print(5**10)


if __name__ == '__main__':
    sys.exit(main(sys.argv))


