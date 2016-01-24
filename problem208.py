#!/usr/bin/env python3

from functools import reduce
from math import factorial
import operator
import sys


def sq(n):
    return n * n


def prod(factors):
    return reduce(operator.mul, factors, 1)


def choose(n, *rs):
    f = factorial

    return f(n) // prod(map(f, *rs))


def count_paths(sides, path_length):
    chains = path_length // sides

    print("count_paths", sides, path_length, chains)

    f = factorial

    a = f(path_length) // f(sides) ** chains

    total_pairs = sides * sides
    adjacent_pairs = 2 * sides
    equal_pairs = sides
    non_adjacent_pairs = total_pairs - (adjacent_pairs + equal_pairs)

    b = sq(sides) * non_adjacent_pairs * f(path_length-2) // f(sides) ** chains

    print(total_pairs, adjacent_pairs, equal_pairs, non_adjacent_pairs)

    c = equal_pairs * f(path_length-2) // (f(sides-2) * f(sides) ** (chains - 1))



    return a, b, c, a-b, a - (b + c)


def main():
    print(5, count_paths(5, 5))
    #print(25, count_paths(5, 25))

    print("------------")
    #a = choose(5, [2, 2, 3])
    #print(a)


if __name__ == "__main__":
    sys.exit(main())
