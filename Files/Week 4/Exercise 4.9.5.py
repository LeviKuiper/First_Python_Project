import turtle


def draw_maze(beast, width, size):
    init = width
    for i in range(size):
        beast.forward(init)
        beast.right(90)
        init += width


def draw_turnymaze(beast, width, size):
    init = width
    for i in range(size):
        beast.forward(init)
        beast.right(89)
        init += width

# main


screen = turtle.Screen()
screen.bgcolor("light gray")

line = turtle.Turtle()
width = 1
size = 360

draw_turnymaze(line, width, size)

screen.mainloop()