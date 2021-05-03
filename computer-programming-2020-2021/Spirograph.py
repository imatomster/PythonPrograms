import turtle
import random

tommy = turtle.Turtle()
tommy.shape("turtle")
tommy.shapesize(1)
tommy.speed(0)

angle = 0
rotAngle = 5
length = 0;

def draw():
    tommy.penup()
    tommy.forward(100)
    tommy.right(90)
    tommy.pendown()
    tommy.forward(length)
    tommy.penup()
    tommy.right(180)
    tommy.forward(length)
    tommy.right(270)
    tommy.forward(100)
    tommy.right(180)
    tommy.pendown()

while(angle < 360):
    length = random.randint(300, 375)
    tommy.pensize(random.randint(1,9))
    tommy.pencolor(random.random(),random.random(),random.random())
    draw()

    tommy.right(rotAngle)
    angle += rotAngle

tommy.pencolor(0,0,0)
tommy.pensize(10)

tommy.penup()
tommy.right(90)
tommy.forward(100)
tommy.pendown()
tommy.right(270)
tommy.circle(100)
tommy.right(270)
tommy.penup()
tommy.forward(100)
