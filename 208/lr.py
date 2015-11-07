#!/usr/bin/env python3

import collections
import itertools
import sys


def roll_right(s):
    """RRLR => RRRL"""
    return s[-1] + s[:-1]


def roll_left(s):
    """RRLR => RRRL"""
    return s[1:] + s[0]


def reduce(s):
    lowest = s

    for n in range(len(s)):
        s = roll_left(s)
        if s < lowest:
            lowest = s

    return lowest


def roll(s):
    if not 'L' in s:
        return s

    if not 'R' in s:
        return s

    while 'R' == s[-1]:
        s = roll_right(s)

    while 'L' == s[0]:
        s = roll_left(s)

    return s


def main(args):
    for line in sys.stdin:
        print(reduce(line.strip()))


if __name__ == '__main__':
    sys.exit(main(sys.argv))

