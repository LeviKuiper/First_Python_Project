import turtle


def draw_stars(beast, side, points):
    for i in range(points):
        turtle.forward(side)
        turtle.right(720/points)


def draw_bigstar(beast, bigside, side, points):
    for i in range(points):
        draw_stars(beast, side, points)
        beast.penup()
        beast.forward(bigside)
        beast.right(720/points)
        beast.pendown()


window = turtle.Screen()
window.bgcolor("light gray")

potato = turtle.Turtle()

side = 100
bigside = 350
points = 5

for i in range(points):
    draw_stars(potato, side, points)
    potato.penup()
    potato.forward(bigside)
    potato.right(720 / points)
    potato.pendown()


draw_bigstar(potato, 350, 100, 5)

window.mainloop()