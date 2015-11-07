#!/usr/bin/env python3

import random
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
    print("reset")
    t.reset()
    return 0


def pent(t, count, size, c):
    t.pencolor('red')
    t.pendown()
    if c == 'r':
        count += 1
        t.circle(-36, 72)
    else:
        count -= 1
        t.circle(36, 72)

    return count



def doCommand(t, count, size, c):
    if 'c' == c:
        return reset(t)
    else:
        return pent(t, count, size, c)


def main(args):
    # Create screen and turtle.
    screen = turtle.Screen()
    screen.title('Square Demo')
    screen_x, screen_y = screen.screensize()
    t = turtle.Turtle()

    # Uncomment to draw the graphics as quickly as possible.
    t.speed(0)
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

        count = doCommand(t, count, length, c)
        count = count % 5
        print(c, count, end=", ", flush=True)
        c = getch()



if __name__ == '__main__':
    sys.exit(main(sys.argv))

