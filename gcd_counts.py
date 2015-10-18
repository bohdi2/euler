#!/usr/bin/env python3

from collections import defaultdict
import fractions
import sys
from functools import lru_cache


def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x


def range1(n):
    return range(1, n+1)


# Check if a number is prime or not
def is_prime(n):
    return not (n < 2 or any(n % i == 0 for i in range(2, int(n ** 0.5) + 1)))


def count_gcds(n):
    counts = defaultdict(int)

    # counts[1]=2
    for x in range1(n):
        for y in range1(n):
            counts[gcd(x, y)] += 1

    return counts


def print_gcds(counts):

    for key, value in counts.items():
        print("%d, %d" % (key, value))


def main(argv):

    limit = 50

    def format_elements(iter):
        return "".join(["{0: >3} ".format(ii) for ii in iter])

    def format_line(prefix, line):
        return "{0:<3}: {1}".format(prefix, line)

    print(format_line("foo", format_elements(range(1,limit+1))))

    for n in range(limit+1):
        counts = count_gcds(n)
        pretty = format_elements(counts.values())
        print(format_line(n, pretty))

    print(format_line("foo", format_elements(range(1,limit+1))))





if __name__ == "__main__":
    main(sys.argv)

