# imports
import turtle
from random import *
# screen setups
screen = turtle.Screen()
screen.setup(0.5,0.6)

# turtle setups
tommy = turtle.Turtle()
tommy.shape("turtle")
tommy.speed(0)
tommy.penup()

# var setups
randomArr = ["YES", "NO", "PERHAPS"]
response = "start"

def drawTurtle():
    if(response == "start"):
        tommy.color('purple')
        tommy.turtlesize(10)
        tommy.stamp()
        tommy.turtlesize(1)
        tommy.color('black')
        tommy.goto(0,0)
        tommy.write("ASK A QUESTION DONT BE SHY", align="center", font=("Arial",40,"bold"))
        tommy.color('purple')
        return
    elif(response == randomArr[0]):
        tommy.color('green')  
    elif(response == randomArr[1]):
        tommy.color('brown')
    elif(response == randomArr[2]):
        tommy.color('yellow')
    
    tommy.turtlesize(10)
    tommy.stamp()
    tommy.turtlesize(1)

def drawAngryTurtle():
    tommy.color("red")
    tommy.stamp()
    tommy.turtlesize(1)
    
def prompt():
    ans = screen.textinput("ASK TURTLE NOW", "Or type 'turtlesuck' to quit")
    turtle.clearscreen()

    if(ans == "turtlesuck"):
        tommy.turtlesize(27)
        drawAngryTurtle()
        tommy.color("black")
        tommy.goto(0,0)
        tommy.write("TURTLE SAYS HOW DARE YOU", align="center", font=("Arial",40,"bold"))
    elif(ans == "" or ans == None):
        tommy.turtlesize(20)
        drawAngryTurtle()
        tommy.color("black")
        tommy.write("SAY SOMETHING OR ELSE", align="center", font=("Arial",40,"bold"))
        tommy.goto(0,-50)
        tommy.write("TURTLE WONT LET U LEAVE", align="center", font=("Arial",40,"bold"))
        tommy.goto(0,0)
        prompt()
    else:
        global response
        response = randomArr[randint(0,2)]
        drawTurtle()
        tommy.color("black")
        tommy.goto(0,100)
        tommy.write("You asked: "+ans, align="center", font=("Arial",40,"bold"))
        tommy.goto(0,0)
        tommy.write("TURTLE SAYS "+response, align="center", font=("Arial",30,"bold"))
        prompt()

    tommy.goto(0,0)

drawTurtle()
prompt()
