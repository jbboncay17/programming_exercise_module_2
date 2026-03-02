import turtle

t = turtle.Turtle()
screen = turtle.Screen()

screen.bgcolor("black")
t.speed(0)
t.hideturtle()

colors = ["orange", "white"]

for i in range(122):
    t.goto(0, 0)
    t.color(colors[i % 2])
    t.forward(130)
    t.left(3)
    t.circle(40)
    t.forward(130)
    t.right(180)

turtle.done()
