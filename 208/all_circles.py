#!/usr/bin/env python3

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


def reset(t):
    t.reset()
    t.pencolor('red')


def lr(n, path_length):
    for count in range(path_length-1, -1, -1):
        if 2 ** count & n:
            print("L", end="")
        else:
            print("R", end="")
    print()


def left(t):
    t.dot("black")
    t.circle(36, 72)


def right(t):
    t.dot("black")
    t.circle(-36, 72)


def loop(t, path_length):
    reset(t)

    for n in range(2 ** path_length):
        p = n
        reset(t)

        for count in range(path_length-1, -1, -1):
            if 2 ** count & n:
                left(t)
            else:
                right(t)

            p = p//2

        if int(t.pos()[0]) == 0 and int(t.pos()[1]) == 0:
            lr(n, path_length)


def main(args):
    # Create screen and turtle.
    screen = turtle.Screen()
    screen.title('Square Demo')
    screen_x, screen_y = screen.screensize()
    t = turtle.Turtle()

    # Uncomment to draw the graphics as quickly as possible.
    #t.speed(0)
    turtle.mode("logo")

    # Draw a set of nested squares, varying the color.
    # The squares are 10%, 20%, etc. of half the size of the canvas.
    length = (screen_y / 2) / 10 * 3
    t.pensize(3)

    count = 0
    c = getch()
    while c:
        if 'q' == c:
            break

        loop(t, int(c) * 5)

        c = getch()



if __name__ == '__main__':
    sys.exit(main(sys.argv))

