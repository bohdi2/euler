#!/usr/bin/env python3

from collections import namedtuple
import sys

import time

def timeit(method):

    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        print('%r (%r, %r) %2.2f sec' % (method.__name__, args, kw, te-ts))
        return result

    return timed

Fraction = namedtuple('Fraction', ['n', 'd'])

class Farey:
    def __init__(self, n):
        self.n = n

    def next_fraction(self, start, end):
        (a, b) = start
        (c, d) = end
        k = (self.n -d)//b
        return k*a + c, k*b + d

    def farey(self, start=(0, 1), end=(1, 1)):
        n = self.n
        (a, b) = start
        (c, d) = self.next_fraction(start, end)

        count = 0

        while (c, d) != end:
            k = (n + b)//d
            a, b, c, d = c, d, k*c - a, k*d - b
            count += 1

        return count

    def __call__(self, start, end):
        return self.farey(start, end)


class RecursiveTree():
    def __init__(self, n):
        self.n = n

    def apply(self, start, stop):
        (a, b) = start
        (c, d) = stop

        #print("%d, %s, %s, %d" % (n, start, stop, (b+d)>n))
        if b+d > self.n:
            return 0

        else:
            mediant = (a+c, b+d)
            #print('"%s" -> "%s"' % (start, mediant))
            #print('"%s" -> "%s"' % (stop, mediant))
            l = self.apply(start, mediant)
            r = self.apply(mediant, stop)
            return l + r + 1


class StackTree():
    def __init__(self, n):
        self.n = n
        self.stack = []

    def apply(self, start, stop):
        n = self.n
        stack = self.stack
        count = 0

        stack.append((start, stop))

        while stack:
            (start, stop) = stack.pop()
            (a, b) = start
            (c, d) = stop

            if b+d > n:
                continue

            mediant = (a+c, b+d)
            #print('"%s" -> "%s"' % (start, mediant))
            #print('"%s" -> "%s"' % (stop, mediant))
            count += 1
            stack.append((start, mediant))
            stack.append((mediant, stop))

            #print("  n: %d, start: %s, stop: %s, mediant: %s, count: %d" % (self.n, start, stop, mediant, count))

        return count


class Problem73():
    def solve(self):
        start = (1, 3)
        stop = (1, 2)

        limit=16000

        for n in range(limit, limit+1):
            #print("start stop: %s, %s" % (start, stop))
            print("%d, %d" % (n, self.farey(n, start, stop)))
            #print("%d, %d" % (n, self.recursive_tree(n, start, stop)))
            print("%d, %d" % (n, self.deque_tree(n, start, stop)))

    @timeit
    def farey(self, n, start, stop):
        function = Farey(n)
        return function(start, stop)

    @timeit
    def recursive_tree(self, n, start, stop):
        function = RecursiveTree(n)
        return function.apply(start, stop)

    @timeit
    def deque_tree(self, n, start, stop):
        function = StackTree(n)
        return function.apply(start, stop)


def main():
    problem = Problem73()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())