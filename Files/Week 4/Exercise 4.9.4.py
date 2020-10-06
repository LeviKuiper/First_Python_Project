import turtle


def draw_square(beast, size):
    for i in range(4):
        beast.forward(size)
        beast.left(90)


# Main

screen = turtle.Screen()
screen.bgcolor("light gray")

circle = turtle.Turtle()
length = 20

times = 25

for j in range(times):
    draw_square(circle, 50)
    circle.left(360/times)

screen.mainloop()