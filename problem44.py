#!/usr/bin/env python3

from collections import Counter
from itertools import combinations
from itertools import count
from itertools import takewhile

import string


def p(n):
    return n * (3 * n - 1) // 2

def pg():
    ii = 0
    while True:
        yield p(ii)
        ii += 1



def main():
    add = set()
    minus = set()
    cache = []

    for p in takewhile(lambda p: p < 4000, pg()):
        #print(ii)
        for (i, j) in combinations(cache, 2):
            if i >= j or j>=p:
                print(i, j, p)

            if i != 0 and (i + j) == p:
                add.add((i, j))
                #print("add", ii, pp)

            if i != 0 and (j == p - j):
                minus.add((i, j))
                #print("sub", ii, pp, pp[1]-pp[0])

        cache.append(p)

    best = None
    n = 1000
    for pp in add & minus:
        if pp[1] - pp[0] < n:
            best = pp
            n = pp[1] - pp[0]

    print(n, best)






if __name__ == "__main__":
    main()
