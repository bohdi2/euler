#!/usr/bin/env python3

from functools import wraps
import sys
from time import time


def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print('%2.4f sec => ' % \
              (te - ts), end="")
        return result

    return wrap






@timing
def sum1(limit, d1, d2):
    sum = 0

    for n in range(1, limit):
        if n % d1 == 0 or n % d2 == 0:
            sum += n

    return sum


@timing
def sum2(limit, d1, d2):
    return sum([n for n in range(1, limit) if n % d1 == 0 or n % d2 == 0])


@timing
def sum3(limit, d1, d2):
    return sum(g(limit, d1, d2))


def g(limit, d1, d2):
    for n in range(1, limit):
        if n % d1 == 0 or n % d2 == 0:
            yield n
    return


@timing
def sum4(n, d1, d2):
    return d1 * t(n // d1) \
           + d2 * t(n // d2) \
           - d1 * d2 * t(n // (d1 * d2))


def t(n):
    return n * (n + 1) // 2



def main(argv):
    million = 1000000
    billion = 1000 * million
    trillion = 1000 * billion


    #print("sum_1(million):      %d" % sum_1(million, 3, 5))
    #print("sum_1(10 million):   %d" % sum_1(10 * million, 3, 5))
    #print("sum_1(100 million):  %d" % sum_1(100 * million, 3, 5))
    #print("sum_1(billion):      %d" % sum_1(billion, 3, 5))


    #print("For loop:  %d" % sum_1(limit, 3, 5))
    #print("List comp: %d" % sum_2(limit, 3, 5))
    #print("Generator: %d" % sum_3(limit, 3, 5))

    print("sum_1(million):      %d" % sum1(million, 3, 5))
    print("sum_1(10 million):   %d" % sum1(10 * million, 3, 5))
    print("sum_1(100 million):  %d" % sum1(100 * million, 3, 5))
    print("sum_1(billion):      %d" % sum1(billion, 3, 5))

    print("-----")
    print("sum_10(million):    %d" % sum10(million, 3, 5))
    print("sum_10(billion):    %d" % sum10(billion, 3, 5))
    print("sum_10(trillion):   %d" % sum10(trillion, 3, 5))


if __name__ == "__main__":
    main(sys.argv)
