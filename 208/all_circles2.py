#!/usr/bin/env python3

import collections
import itertools
import sys
import turtle


def _find_getch():
    try:
        import termios
    except ImportError:
        # Non-POSIX. Return msvcrt's (Windows') getch.
        import msvcrt
        return msvcrt.getch

    # POSIX system. Create and return a getch that manipulates the tty.
    import sys, tty
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


def lr(p):
    n = 0
    for c in p:
        n = 2*n
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

    for n in range(len(s)):
        s = roll_left(s)
        if s < lowest:
            lowest = s

    return lowest


def reset(t):
    t.reset()
    t.pencolor('red')


def left(t):
    t.dot("black")
    t.circle(36, 72)


def right(t):
    t.dot("black")
    t.circle(-36, 72)


def loop(t, path_length):
    reset(t)

    cache = set()

    for p in itertools.product("RL", repeat=path_length):
        c = collections.Counter(p)
        if c['R'] % 5 != 0:
            continue

        r = reduce(p)
        if r in cache:
            continue
        cache.add(r)

        reset(t)

        for direction in p:
            if 'L' == direction:
                left(t)
            else:
                right(t)

        n = lr(p)
        if int(t.pos()[0]) == 0 and int(t.pos()[1]) == 0:
            print("".join(p))



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

    loop(t, 20)





if __name__ == '__main__':
    sys.exit(main(sys.argv))

