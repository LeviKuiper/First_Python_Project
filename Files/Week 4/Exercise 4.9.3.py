import turtle


def draw_polygon(animal, color, corners, size):
    animal.color(color)
    for i in range(corners):
        animal.forward(size)
        animal.left(360/corners)


window = turtle.Screen()
window.bgcolor("light gray")

potato = turtle.Turtle()

draw_polygon(potato, "blue", 8, 50)

window.mainloop()
