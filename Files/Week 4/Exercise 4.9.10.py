import turtle


def draw_stars(animal, side, points):
    for i in range(points):
        animal.forward(side)
        animal.right(720/points)


def draw_bigstar(animal, bigside, side, points):
    for i in range(points):
        animal.pendown()
        draw_stars(animal, side, points)
        animal.penup()
        animal.forward(bigside)
        animal.right(720/points)



window = turtle.Screen()
window.bgcolor("light gray")

potato = turtle.Turtle()

draw_bigstar(potato, 350, 100, 5)

window.mainloop()