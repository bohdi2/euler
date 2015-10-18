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
        print('func:%r args:[%r, %r] took: %2.4f sec' % \
              (f.__name__, args, kw, te - ts))
        return result

    return wrap






#@timing
def sum_1(limit, d1, d2):
    sum = 0

    for n in range(1, limit):
        if n % d1 == 0 or n % d2 == 0:
            sum = sum + n

    return sum


#@timing
def sum_2(limit, d1, d2):
    return sum([n for n in range(1, limit) if n % d1 == 0 or n % d2 == 0])


#@timing
def sum_3(limit, d1, d2):
    return sum(g(limit, d1, d2))


def g(limit, d1, d2):
    for n in range(1, limit):
        if n % d1 == 0 or n % d2 == 0:
            yield n
    return


#@timing
def sum_10(limit, d1, d2):
    return triangle(limit - 1, skip=d1) + triangle(limit, skip=d2) - triangle(limit, skip=d1 * d2)


def triangle(limit, skip=1):
    n = limit // skip
    return skip * n * (n + 1) // 2



def main(argv):
    million = 1000000
    billion = 1000 * million
    limit = billion // 5

    print("For loop:  %d" % sum_1(limit, 3, 5))
    print("List comp: %d" % sum_2(limit, 3, 5))
    print("Generator: %d" % sum_3(limit, 3, 5))
    print("Math:      %d" % sum_10(limit, 3, 5))

if __name__ == "__main__":
    main(sys.argv)
