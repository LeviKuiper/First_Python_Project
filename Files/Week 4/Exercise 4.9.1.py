import turtle


def draw_square(turtle, size):
    for i in range(4):
        turtle.forward(20)
        turtle.left(90)


# Main

screen = turtle.Screen()
screen.bgcolor("light gray")

square = turtle.Turtle()

for i in range(4):
    draw_square(square, 20)
    square.penup()
    square.forward(40)
    square.pendown()

screen.mainloop()