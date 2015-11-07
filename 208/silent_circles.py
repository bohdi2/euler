#!/usr/bin/env python3

import collections
import itertools
import sys
import turtle


class Turtle:
    def __init__(self, limit):
        self.direction = 0
        self.visits = [0, 0, 0, 0, 0]
        self.goal = [limit] * 5

    def clear(self):
        self.direction = 0
        self.visits = [0, 0, 0, 0, 0]

    def isGood(self):
        return self.visits == self.goal

    def left(self):
        self.direction = (self.direction + 1) % 5
        self.visits[self.direction] += 1

    def right(self):
        self.direction = (self.direction - 1) % 5
        self.visits[self.direction] += 1

    def move(self, c):
        if 'L' == c:
            self.left()
        else:
            self.right()


def roll_right(s):
    """RRLR => RRRL"""
    return s[-1] + s[:-1]


def roll_left(s):
    """RRLR => RRRL"""
    return s[1:] + s[0]


def reduce(s):
    s = "".join(s)
    lowest = s

    for n in range(len(s)):
        s = roll_left(s)
        if s < lowest:
            lowest = s

    return lowest


def loop(t, path_length):

    for p in itertools.product("RL", repeat=path_length):
        c = collections.Counter(p)
        if c['R'] % 5 != 0:
            continue

        r = reduce(p)

        t.clear()

        for direction in p:
            t.move(direction)

        if t.isGood():
            print("".join(p))



def main(args):
    path_length = 30
    t = Turtle(path_length//5)

    loop(t, path_length)





if __name__ == '__main__':
    sys.exit(main(sys.argv))

