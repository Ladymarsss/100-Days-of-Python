import turtle as t
import random as ra
t.title("Spirograph")
t.bgcolor("black")
t.shape("turtle")
t.color("white")
t.speed(100)
t.colormode(255)

def random_color():
    r = ra.randint(0, 255)
    g = ra.randint(0, 255)
    b = ra.randint(0, 255)
    rgb = (r, g, b)
    return rgb

for x in range(100):
    t.color(random_color())
    t.circle(100)
    t.up()
    t.left(5)
    t.down()

t.exitonclick()
