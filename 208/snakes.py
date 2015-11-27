#!/usr/bin/env python3

import sys

def find_significant_digit(n):
    while n > 9:
        n = n // 10

    return n


def all_equal(s):
    return s.count(s[0]) == len(s)

def looped(sides, n):
    d = n % 10
    n = find_significant_digit(n)

    if n > d:
        return (sides-1, 0) == (n, d) or (1, 0) == (n, d)
    else:
        return (sides-1, 0) == (d, n) or (1, 0) == (d, n)


def to_snake(ns):
    last = 0
    s = ""

    for n in ns:
        if (n<last):
            s += 'R'
        else:
            s += 'L'
        last = n

    return s




def break_down(sides, n, path, snake):
    c = [0] * sides

    t = n
    while t > 0:
        c[t % 10] += 1
        t = t // 10

    #print(sides, n, c, all_equal(c), looped(sides, n))
    if all_equal(c) and looped(sides, n):
        print(path, snake)


def r(sides, depth, n, path, snake):
    if depth == 0:
        break_down(sides, n, path, snake)
        return

    d = n % 10
    n = n * 10
    r(sides, depth-1, n + (d-1) % sides, path + str(d+1), snake + "L")
    r(sides, depth-1, n + (d+1) % sides, path + str(d+1), snake + "R")


def main(args):
    depth_factor = int(args[1])
    sides = int(args[2])
    depth = sides * depth_factor
    r(sides, depth, 0, "", "")


if __name__ == '__main__':
    sys.exit(main(sys.argv))

