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
    expected = {'1' : 2, '2' : 2, '3' : 2, '4' : 2, '5' : 2}

    print("All permutations of 10: ",   9765625)
    print("All permutations of pairs: ", 113400)
    print("All 11s: ", 22680)
    print("All 12s: ", 42840)

    length = 10
    count = 0
    for p in itertools.product("12345", repeat=length):
        p = "".join(p)
        c = collections.Counter(p)
        #print(c)
        if c == expected:
            print(p)


if __name__ == '__main__':
    sys.exit(main(sys.argv))



