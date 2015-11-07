#!/usr/bin/env python3

import collections
import itertools
import sys
import turtle


class Turtle:
    def __init__(self, sides, limit):
        self.sides = sides
        self.direction = 0
        self.visits = [0] * sides
        self.goal = [limit] * sides

    def clear(self):
        self.direction = 0

        self.visits = [0] * self.sides

    def is_good(self):
        return self.visits == self.goal

    def left(self):
        self.direction = (self.direction + 1) % self.sides
        self.visits[self.direction] += 1

    def right(self):
        self.direction = (self.direction - 1) % self.sides
        self.visits[self.direction] += 1

    def move(self, c):
        if 'L' == c:
            self.left()
        else:
            self.right()


def reduce(s):
    return "".join(s)


def draw(sides, depth):
    t = Turtle(sides, depth)
    count = 0
    for p in itertools.product("RL", repeat=sides*depth):
        rs = 0
        for c in p:
            if c == 'R':
                rs += 1

        if rs % sides != 0:
            continue

        r = reduce(p)

        t.clear()

        for direction in p:
            t.move(direction)

        if t.is_good():
            #print("".join(p), t.direction)
            count += 1
    return count


def main(args):
    sides_list = range(1,19,2)
    depth_list = [1, 2]

    #sides_list = [2]
    #depth_list = [2]

    print("-------------- depth ------------")
    for depth in ['x'] + depth_list:
        print(depth, end="\t")
    print()
    for sides in sides_list:
        print(sides, end="\t")
        for depth in depth_list:
            print(draw(sides, depth), end="\t", flush=True)
        print()





if __name__ == '__main__':
    sys.exit(main(sys.argv))

