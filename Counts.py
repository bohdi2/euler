#!/usr/bin/env python3

import math


def count(n):
    return sum([int(c) for c in str(n)])

def id(n):
    return n

def square(n):
    return n*n

def test(f, iter):
    prev = 0

    for ii in iter:
        n = f(ii)
        c = count(n)
        print("%d => %d, %d" % (ii, c, (c - prev)))
        prev = c

start = 0

test(square, range(start, start + 25))


cache = {}

for n in range(0, 100000, 1):
    cn = count(n)
    if cn not in cache:
        cache[cn] = []
    cache[cn].append(n)

# for ii in range(10):
 #    print("%d %d" % (ii, len(cache[ii])))

