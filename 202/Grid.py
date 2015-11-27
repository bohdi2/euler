#!/usr/bin/env python3

import math
import turtle
from itertools import chain
from itertools import islice


def _find_getch():
    import termios

    # POSIX system. Create and return a getch that manipulates the tty.
    import sys
    import tty

    def _getch():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

    return _getch


getch = _find_getch()


def take(n, iterable):
    """Return first n items of the iterable as a list"""
    return list(islice(iterable, n))


def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x


class Label:

    def __init__(self, x, y):
        self.abc = "CBA"[(x - y) % 3]
        if self.abc == 'C':
            self.color = "red" if gcd(x, y) == 1 else "blue"
        else:
            self.color = "black"


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, t):
        # print("drawing", self.x, self.y)
        t.up()
        t.goto(self.x, self.y)
        t.down()
        t.dot()

    def __str__(self):
        return "({}, {})".format(self.x, self.y)


class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, t):
        self.p1.draw(t)
        t.down()
        t.goto(self.p2.x, self.p2.y)
        self.p2.draw(t)


class Model:
    def __init__(self, size):
        self.size = size
        self.dots = dict()
        self.x_lines = []
        self.y_lines = []
        self.d_lines = []

        for x in range(size):
            for y in range(size - x):
                self.dots[Point(x, y)] = Label(x, y)

        for y in range(size):
            self.x_lines.append(Line(Point(0, y), Point(self.size - y - 1, y)))

        for x in range(size):
            self.y_lines.append(Line(Point(x, 0), Point(x, self.size - x - 1)))

        for d in range(size):
            self.d_lines.append(Line(Point(0, d), Point(d, 0)))


class Translator:
    def __init__(self, origin, segment):
        self.origin = origin
        self.segment = segment

    def translate_point(self, p):
        x = self.origin.x + self.segment * p.x
        y = self.origin.y + self.segment * p.y
        return Point(x, y)

    def translate_line(self, l):
        return Line(self.translate_point(l.p1), self.translate_point(l.p2))

    def translate_grid(self, model):
        dots = dict()

        for point in model.dots:
            dots[point] = self.translate_point(point), model.dots[point]

        x_lines = map(self.translate_line, model.x_lines)
        y_lines = map(self.translate_line, model.y_lines)
        d_lines = map(self.translate_line, model.d_lines)

        return View(self.origin, model.size, dots, x_lines, y_lines, d_lines)


class View:
    def __init__(self, origin, size, dots, x_lines, y_lines, d_lines):
        self.origin = origin
        self.size = size
        self.dots = dots
        self.x_lines = x_lines
        self.y_lines = y_lines
        self.d_lines = d_lines

    def draw(self, t):
        for p, l in self.dots.values():
            t.color(l.color)
            p.draw(t)
            t.down()
            t.write(l.abc)
            t.color("black")

        for l in chain(self.x_lines, self.y_lines, self.d_lines):
            l.draw(t)


if __name__ == '__main__':
    # Create screen and turtle.
    screen = turtle.Screen()
    screen.title('202 Demo')
    screen_x, screen_y = screen.screensize()

    # Uncomment to draw the graphics as quickly as possible.

    turtle.mode("standard")

    # Draw a set of nested squares, varying the color.
    # The squares are 10%, 20%, etc. of half the size of the canvas.

    m = Model(12)

    t0 = Translator(Point(-400, -300), 50)
    v0 = t0.translate_grid(m)
    v0.draw(turtle.Turtle())


    c = getch()
    while c:
        if 'q' == c:
            break

        c = getch()

