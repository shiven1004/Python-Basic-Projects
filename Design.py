import turtle
turtle.bgcolor("black")

turtle.speed(0)
turtle.pensize(4)
turtle.pencolor("cyan")


def draw_circle(radius):
    for i in range(10):
        turtle.circle(radius)
        radius -= 4


def draw_design():
    for i in range(10):
        draw_circle(150)
        turtle.right(36)


draw_design()
turtle.done()
