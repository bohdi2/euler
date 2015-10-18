#!/usr/bin/env python3

import argparse
import functools
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


def isPandigital(n):
    return "0123456789" == ''.join(sorted(str(n)))

def pandigital():
    for n in range(123456789, 9876543210):
        if isPandigital(n):
            #print("slow", n)
            yield n


def pandigital1(step=1):
    steps = [n for n in range(1000) if n % step == 0]

    for ii in range(123456, 9876543):
        for jj in steps:
            n = ii * 1000 + jj
            if isPandigital(n):
                yield n


def pandigital3():
    digits = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

    def piter(remaining_digits, result):
        if not remaining_digits:
            yield result

        else:
            for digit in remaining_digits:
                new_digits = set(remaining_digits) - {digit}
                new_result = list(result)
                new_result.append(digit)
                yield from piter(new_digits, new_result)

    return piter(digits, [])


def test(n, divisor, prime):
    return ((n//divisor) % 1000) % prime == 0


def test_all(n):
    return (test(n, 1, 17) and
            test(n, 10, 13) and
            test(n, 100, 11) and
            test(n, 1000, 7) and
            test(n, 10000, 5) and
            test(n, 100000, 3) and
            test(n, 1000000, 2))


def test3(result, index, prime):
    n = 100 * result[index-1] + 10 * result[index] + result[index+1]
    return n % prime == 0


def test_all3(result):
    return (test3(result, 8, 17) and
            test3(result, 7, 13) and
            test3(result, 6, 11) and
            test3(result, 5, 7) and
            test3(result, 4, 5) and
            test3(result, 3, 3) and
            test3(result, 2, 2))


class BruteForce:

    def __call__(self):
        answer = 0

        for n in pandigital():
            if test_all(n):
                answer += n
                print(n, answer)

        return answer


class BruteForce17:

    def __call__(self):
        answer = 0

        for n in pandigital1(17):
            if test_all(n):
                answer += n
                print(n, answer)

        return answer

class BruteForce3:

    def __call__(self):
        answer = 0

        for result in pandigital3():
            if test_all3(result):
                n = functools.reduce(lambda accum, item: 10*accum + item, result, 0)
                answer += n
                print(n, answer)

        return answer


class Problem43():

    @timeit
    def sanity_checks(self):
        return test_all(1406357289)

    @timeit
    def sanity_checks2(self):
        return test_all(1406357288)

    @timeit
    def brute_force(self):
        # 2.4 hours
        function = BruteForce()
        return function()

    @timeit
    def brute_force17(self):
        # 9.1 minutes
        function = BruteForce17()
        return function()

    @timeit
    def brute_force3(self):
        # 8 seconds
        function = BruteForce3()
        return function()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("command")
    args = parser.parse_args()
    problem = Problem43()

    if "tests" == args.command:
        # print("sanity checks", problem.sanity_checks())
        # print("sanity checks", problem.sanity_checks2())
        # print("17s", [n for n in range(1000) if n%17 == 0])

        for n in pandigital3():
            print("m", n)

    elif "brute1" == args.command:
        print("brute_force", problem.brute_force())

    elif "brute17" == args.command:
        print("brute_force17", problem.brute_force17())

    elif "brute3" == args.command:
        print("brute_force3", problem.brute_force3())

    elif "all" == args.command:
        print("brute_force", problem.brute_force())
        print("brute_force17", problem.brute_force17())
        print("brute_force3", problem.brute_force3())


if __name__ == '__main__':
    sys.exit(main())
