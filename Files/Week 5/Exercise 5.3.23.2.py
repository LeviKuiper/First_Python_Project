import turtle


screen = turtle.Screen()
tess = turtle.Turtle()
alex = tess
alex.color("red")

alex.forward(90)
tess.forward(-90)

# Alex and Tess are stored as the exact same "turtle", they have been aliassed

screen.exitonclick()