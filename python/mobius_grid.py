#!/usr/bin/env python3

from tkinter import *
import itertools

def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x


class Point(object):
    def __init__(self, x, y, fg="red"):
        self.x = x
        self.y = y
        self.rank = max(x, y)
        self.fg=fg
        self.gcd = gcd(x, y)

    def __str__(self):
        return "%d,%d" % (self.x, self.y)

    def isEdge(self):
        return self.x == 0 or self.y == 0



class Color(object):
    def __init__(self, fg, bg="white"):
        self.fg = fg
        self.bg = bg

    def __str__(self):
        return "(%s,%s)" % (self.fg, self.bg)


class GuiModel(dict):
    def __init__(self, n):

        for p in [Point(*t) for t in itertools.product(range(n), range(n))]:
            if p.isEdge():
                self[p] = Color("blue", "grey")
            else:
                self[p] = Color("blue")


def create_buttons(gui_model):
    buttons = {}

    font1 = ("Arial", 14, "bold")

    for p in gui_model:
        if p.isEdge():
            button = Button(frame, font=font1, fg="black", bg="white", width=1, height=1)
            button.configure(text="%d" % (p.x + p.y))
        else:
            button = Button(frame, font=font1, fg=gui_model[p].fg, bg="white", width=1, height=1)
            button.configure(text="%d" % p.gcd)
            button.configure(command=make_handler(p))

        button.grid(row=p.y, column=p.x)
        buttons[p] = button

    return buttons


def make_handler(p):
    """makeHandler constructs a handler function for a new button.
       parameters:
          myrow - an int, the row coordinate where the new button lives
          mycolumn  - an int, the column coordinate where the new button lives
       returns: the handler function customized for a new button
    """
    def handle_button_press():
        repaint_gui(p)

    return handle_button_press


# the VIEW module starts here:

def repaint_gui(p):
    """repaintGUI  repaints the foreground text of all the buttons on the GUI,
       it also updates the displayed count of captures, and if there is a
       winner, it prints a message as to who won.
    """
    global buttons

    for (key, button) in buttons.items():
        if key.isEdge():
            continue

        if key.rank > p.rank:
            # Outer most square
            button.configure(fg="light grey", bg="white")
        elif key.rank > p.rank//p.gcd:
            # Middle Square
            button.configure(fg="white", bg="light grey")
            if (key.gcd == p.gcd):
                button.configure(fg="red")
        else:
            # Inner square
            button.configure(fg="light grey", bg="grey")
            if (key.gcd == p.gcd):
                button.configure(fg="red")
            if (key.gcd == 1):
                button.configure(fg="orange")






window = Tk()
window.title("Pente")
board_size = 25  # Board.size
window.geometry(str(40 * board_size) + "x" + str(40 * board_size))
frame = Frame(window)
frame.grid()

for p in itertools.product(range(3), range(3)):
    print(p)


# label1 = Label(frame, text="Captures =  Y", font=("Arial", 12, "bold"))
# label1.grid(row=0, column=0, columnspan=5)

model = GuiModel(board_size)
buttons = create_buttons(model)

window.mainloop()   # activate GUI
