import turtle as t

t = t.Turtle()

for x in range(15):
    t.forward(10)
    t.up()
    t.forward(10)
    t.down()


t.screen.exitonclick()