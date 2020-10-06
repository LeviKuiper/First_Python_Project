import turtle


def draw_square(beast, size):
    for i in range(4):
        beast.forward(size)
        beast.left(90)


# Main

screen = turtle.Screen()
screen.bgcolor("light gray")

triangle = turtle.Turtle()
length = 20

for j in range(4):
    draw_square(triangle, length)
    triangle.penup()
    triangle.goto(-length/2, -length/2)
    triangle.pendown()
    length += 20

screen.mainloop()


screen.mainloop()
