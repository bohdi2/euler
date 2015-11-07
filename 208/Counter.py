#!/usr/bin/env python3

from collections import Counter
from operator import add
import sys

class State:
    def __init__(self, direction, tokens, path):
        self.direction = direction
        self.tokens = tokens
        self.path = path

    def as_key(self):
        return '"{} {} {}"'.format(self.direction, self.tokens, "") #self.path)

    def left(self):
        d = (self.direction + 1) % 5
        t = self.tokens[:]
        t[d] += -1
        return State(d, t, self.path + "L")

    def right(self):
        d = (self.direction - 1) % 5
        t = self.tokens[:]
        t[d] += -1
        return State(d, t, self.path + "R")

    def __str__(self):
        return '{} {} {}'.format(self.direction, self.tokens, self.path)


class MyCounter:
    def __init__(self, depth, sides):
        self.depth = depth
        self.sides = sides

    def add_counters(self, left, right):
        return map(add, left, right)

    def as_key(self, direction, tokens, path):
        return '"{} {} {}"'.format(direction, tokens, "")


    def count(self):
        return self.add_counters(self.left(State(0, [self.depth] * self.sides, "")),
                                 self.right(State(self.sides-1, [self.depth] * self.sides, "")))

    def left(self, state):
        new_state = state.left()
        parent_key = state.as_key()
        child_key = new_state.as_key()

        if new_state.tokens[new_state.direction] < 0:
            print('{} [color=red]'.format(child_key))
            print('{} -> {} [label=L]'.format(parent_key, child_key))

            return [0] * self.sides

        good = True
        for token in new_state.tokens:
            if token != 0:
                good = False
                break

        if good:
            result = [0] * self.sides
            result[state.direction] = 1
            print('{} [color=green]'.format(child_key))
            print('{} -> {} [label=L]'.format(parent_key, child_key))
            return result

        print('{} -> {} [label=L]'.format(parent_key, child_key))

        return self.add_counters(self.left(new_state), self.right(new_state))

    def right(self, state):
        new_state = state.right()
        parent_key = state.as_key()
        child_key = new_state.as_key()

        if new_state.tokens[new_state.direction] < 0:
            print('{} [color=red]'.format(child_key))
            print('{} -> {} [label=R]'.format(parent_key, child_key))

            return [0] * self.sides

        good = True
        for token in new_state.tokens:
            if token != 0:
                good = False
                break

        if good:
            result = [0] * self.sides
            result[state.direction] = 1
            print('{} [color=green]'.format(child_key))
            print('{} -> {} [label=R]'.format(parent_key, child_key))
            return result

        print('{} -> {} [label=R]'.format(parent_key, child_key))

        return self.add_counters(self.left(new_state), self.right(new_state))




def main(args):

    sides_list = [5]
    depth_list = [1]

    print("digraph G {")
    print("conentrade=true")
    c = MyCounter(2, 5)
    c.count()
    print("}")

    #print("-------------- depth ------------")
    for depth in ['x'] + depth_list:
        #print(depth, end="\t")
        pass
    #print()
    for sides in sides_list:
        #print(sides, end="\t")
        for depth in depth_list:
            c = MyCounter(depth, sides)
            #print(list(c.count()), end="\t", flush=True)
        #print()




if __name__ == '__main__':
    sys.exit(main(sys.argv))


