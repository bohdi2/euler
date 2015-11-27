#!/usr/bin/env python3

import sys


class GraphAccumulator:
    def __init__(self, sides):
        self.sides = sides
        self.counters = [0] * sides
        self.states = []
        self.tree = []

    def init(self, counter):
        self.counters = [0] * counter.sides
        self.states.clear()
        self.tree.clear()

    def update(self, parent, child):
        self.states.append(child)
        self.tree.append((parent, child))

        if child.is_balanced():
            self.counters[child.direction] += 1

    def graph(self):
        s = "digraph G {\n"
        for state in self.states:
            s += '{} [{}]\n'.format(state.as_key(), self.color(state), self.back_ground_color(state))

        for (parent, child) in self.tree:
            s += '{} -> {} [label={}]\n'.format(parent.as_key(), child.as_key(), child.path[-1])

        s += "}"
        return s

    def color(self, state):
        if state.is_balanced() and state.is_snake_balanced():
            return "style=filled fillcolor=green"
        elif state.is_balanced():
            return "style=filled fillcolor=pink"
        elif state.is_lr_balanced():
            return "style=filled fillcolor=orange"
        else:
            return "style=filled fillcolor=white"

    def back_ground_color(self, state):
        if state.is_balanced() and state.is_snake_balanced():
            return "style=filled fillcolor=pink"
        else:
            return "style=filled fillcolor=gray"

    def __str__(self):
        return str(self.counters)


class CounterAccumulator:
    def __init__(self, sides):
        self.sides = sides

        self.counters = [0] * sides
        self.states = []

    def init(self, counter):
        self.green = 0
        self.pink = 0
        self.orange = 0
        self.white = 0
        self.counters = [0] * counter.sides
        self.states.clear()

    def update(self, parent, child):
        self.states.append(child)

    def graph(self):
        for state in self.states:
            if state.is_balanced() and state.is_snake_balanced():
                self.green += 1
            if state.is_balanced():
                self.pink += 1
            if state.is_lr_balanced():
                self.orange += 1
            if not (state.is_balanced() or state.is_snake_balanced()):
                self.white += 1

        return len(self.states), self.green, self.pink, self.orange, self.white

    def __str__(self):
        return self.graph()


class LineAccumulator:
    def __init__(self, depth, sides):
        self.sides = sides
        self.snake_length = depth * sides

        self.counters = [0] * sides
        self.states = []

    def init(self, counter):
        self.counters = [0] * counter.sides
        self.states.clear()

    def update(self, parent, child):
        if child.is_terminal():
            self.states.append(child)

    def graph(self):
        s = ""
        for state in self.states:
            snake = state.path.ljust(self.snake_length, '.')
            numbers = self.snake_to_numbers(snake)

            s += '{} {} {} {}\n'.format(self.tf(state.is_balanced()), self.tf(state.is_snake_balanced()), snake, numbers)

        return s

    def snake_to_numbers(self, snake):
        n = 0
        ns = []
        for s in snake:
            if s == 'L':
                n = (n - 1) % self.sides
                ns.append(n)
            elif s == 'R':
                n = (n + 1) % self.sides
                ns.append(n)
            else:
                break

        return ns

    def tf(self, b):
        if b:
            return 'T'
        else:
            return 'F'

    def __str__(self):
        return self.graph()


class State:
    def __init__(self, sides, direction, tokens, path=""):
        self.sides = sides
        self.direction = direction
        self.tokens = tokens
        self.path = path
        self.type = self.get_type(tokens)

    def as_key(self):
        return '"{}\n{}\n{}"'.format(self.direction, self.tokens, self.path)

    def left(self):
        d = (self.direction + 1) % self.sides
        t = self.tokens[:]
        t[d] += -1
        return State(self.sides, d, t, self.path + "L")

    def right(self):
        d = (self.direction - 1) % self.sides
        t = self.tokens[:]
        t[d] += -1
        return State(self.sides, d, t, self.path + "R")

    def is_balanced(self):
        return self.type == "Balanced"

    def is_unbalanced(self):
        return self.type == "Error"

    def is_terminal(self):
        return self.type != "Node"

    def is_snake_balanced(self):
        return self.is_multiple_of_sides(len(self.path)) and self.is_multiple_of_sides(self.path.count("L"))

    def is_multiple_of_sides(self, n):
        return (n % self.sides) == 0

    @staticmethod
    def get_type(tokens):
        for token in tokens:
            if token < 0:
                return "Error"

        for token in tokens:
            if token > 0:
                return "Node"

        return "Balanced"

    def __str__(self):
        return '{} {} {} {}'.format(self.direction, self.tokens, self.path, self.type)


class MyCounter:
    def __init__(self, depth, sides, accumulator):
        self.depth = depth
        self.sides = sides
        self.accumulator = accumulator

    def as_key(self, direction, tokens, path):
        return '"{} {} {}"'.format(direction, tokens, "")

    def count(self):
        self.accumulator.init(self)
        self.count_p(None, State(self.sides, 0, [self.depth] * self.sides))
        return self.accumulator

    def count_p(self, parent, child):
        if parent:
            self.accumulator.update(parent, child)

        if child.is_terminal():
            return

        self.count_p(child, child.left())
        self.count_p(child, child.right())


def create_counter(depth, sides):
    return MyCounter(depth, sides, CounterAccumulator(sides))


def create_graph(depth, sides):
    return MyCounter(depth, sides, GraphAccumulator(5))


def create_line(depth, sides):
    return MyCounter(depth, sides, LineAccumulator(depth, sides))


def main(args):

    jobs = [(3, [1, 2, 3, 4, 5]),
            (5, [1, 2, 3, 4]),
            (7, [1, 2, 3]),
            (9, [1, 2])
            ]

    jobs = []

    c = create_line(3, 5)
    a = c.count()
    print(a.graph())

    print(jobs)
    for sides, depths in jobs:
        print("----", sides, "----")
        print("total, snake and balanced, balanced, snake")
        for depth in depths:
            c = create_counter(depth, sides)
            a = c.count()
            print(a.graph(), flush=True)
        print()

if __name__ == '__main__':
    sys.exit(main(sys.argv))


