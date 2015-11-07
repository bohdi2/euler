#!/usr/bin/env python3

import collections
import itertools
import sys
import turtle


def lr(p):
    n = 0
    for c in p:
        n = 2 * n
        if c == 'R':
            n += 1
    return n


def roll_right(s):
    """RRLR => RRRL"""
    return s[-1] + s[:-1]


def roll_left(s):
    """RRLR => RRRL"""
    return s[1:] + s[0]


def reduce(s):
    s = "".join(s)
    lowest = s

    #for n in range(len(s)):
    #    s = roll_left(s)
    #    if s < lowest:
    #        lowest = s

    return lowest


def reset(t):
    t.up()
    t.home()
    t.down()


def left(t, arc):
    t.dot("black")
    t.circle(arc//2, arc)


def right(t, arc):
    t.dot("black")
    t.circle(-arc//2, arc)

def end(t):
    t.dot(15, "black")
    #t.write(12)


def draw(t, sides, depth):
    arc = 360 // sides
    reset(t)

    cache = set()

    for p in itertools.product("RL", repeat=sides*depth):
        c = collections.Counter(p)
        if c['R'] % sides != 0:
            continue

        r = reduce(p)
        #if r in cache:
        #    continue
        cache.add(r)

        reset(t)

        for direction in p:
            if 'L' == direction:
                left(t, arc)
            else:
                right(t, arc)

        #n = lr(p)
        end(t)
        print("".join(p), t.pos(), flush=True)
        #if int(t.pos()[0]) == 0 and int(t.pos()[1]) == 0:
        #    print("".join(p))



def main(args):
    # Create screen and turtle.
    screen = turtle.Screen()
    screen.title('Square Demo')
    screen_x, screen_y = screen.screensize()
    t = turtle.Turtle()

    turtle.mode("logo")

    # Draw a set of nested squares, varying the color.
    # The squares are 10%, 20%, etc. of half the size of the canvas.
    length = (screen_y / 2) / 10 * 3
    t.pensize(3)
    t.pencolor('red')

    #draw(t, 2, 2)
    draw(t, 5, 2)






if __name__ == '__main__':
    sys.exit(main(sys.argv))

