#This imports only Screen and Turtle from the module 
from turtle import Screen, Turtle

#This imports everything in the turtle module
# from turtle import *

#Changing the arrrow
turtle = Turtle()
turtle.shape("turtle")
turtle.color("pink")

#Moving the Turtle/Pen (That's a Square)
# turtle.forward(90)
# turtle.left(90)
# turtle.forward(90)
# turtle.left(90)
# turtle.forward(90)
# turtle.left(90)
# turtle.forward(90)

#The same square but simplified
for _ in range(4):
    turtle.forward(100)
    turtle.left(90)
    
#making the screen to stay, until clicked on it
screen = Screen()
screen.exitonclick()