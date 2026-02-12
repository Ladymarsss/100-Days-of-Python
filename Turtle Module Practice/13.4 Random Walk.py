import turtle as t
import random

t.title("Random Walk")
t.bgcolor("black")
t.pensize(10)
t.speed("fastest")

colours = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
direction = [0, 90, 180, 270]

for x in range(200):
    t.color(random.choice(colours))
    t.forward(30)
    t.setheading(random.choice(direction))

t.exitonclick()


