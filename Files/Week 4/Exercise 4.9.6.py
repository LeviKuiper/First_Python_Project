import turtle


def draw_polygon(animal, corners, size):
    for i in range(corners):
        animal.forward(size)
        animal.left(360/corners)


def draw_equitriangle(beast, size):
    draw_polygon(beast, 3, size)


window = turtle.Screen()
window.bgcolor("light gray")

potato = turtle.Turtle()

draw_equitriangle(potato, 50)

window.mainloop()