import turtle

# create a new turtle object called tommy
tommy = turtle.Turtle() 
# make tommy's inital shape a turtle, look up what else turtle's can be
tommy.shape("turtle") 
# initalize tommy's draw speed to be 10
tommy.speed(10)

#Backgroudn of Flag
tommy.color('#b19cd9')
tommy.begin_fill()
tommy.goto(350,200)
tommy.goto(350,-200)
tommy.goto(-350,-200)
tommy.goto(-350,200)
tommy.goto(350,200)
tommy.end_fill()
tommy.home()

#Rectangle
tommy.color('#98FB98')
tommy.begin_fill()
tommy.goto(350,100)
tommy.goto(350,-100)
tommy.goto(-350,-100)
tommy.goto(-350,100)
tommy.goto(350,100)
tommy.end_fill()
tommy.home()

#Top Row Stamp
tommy.penup()
tommy.color('green')

tommy.turtlesize(2)
tommy.goto(300, 150)
tommy.stamp()
tommy.turtlesize(3)
tommy.goto(200, 150)
tommy.stamp()
tommy.turtlesize(2)
tommy.goto(100, 150)
tommy.stamp()
tommy.turtlesize(3)
tommy.goto(0, 150)
tommy.stamp()
tommy.turtlesize(2)
tommy.goto(-300, 150)
tommy.stamp()
tommy.turtlesize(3)
tommy.goto(-200, 150)
tommy.stamp()
tommy.turtlesize(2)
tommy.goto(-100, 150)
tommy.stamp()
tommy.turtlesize(3)
tommy.goto(-0, 150)
tommy.stamp()

#Bot Row Stamp
tommy.turtlesize(2)
tommy.goto(300, -150)
tommy.stamp()
tommy.turtlesize(3)
tommy.goto(200, -150)
tommy.stamp()
tommy.turtlesize(2)
tommy.goto(100, -150)
tommy.stamp()
tommy.turtlesize(3)
tommy.goto(0, -150)
tommy.stamp()
tommy.turtlesize(2)
tommy.goto(-300, -150)
tommy.stamp()
tommy.turtlesize(3)
tommy.goto(-200, -150)
tommy.stamp()
tommy.turtlesize(2)
tommy.goto(-100, -150)
tommy.stamp()
tommy.turtlesize(3)
tommy.goto(-0, -150)
tommy.stamp()

#Middle Row Stamps
tommy.color('purple')
tommy.turtlesize(2)
tommy.goto(300, -50)
tommy.tilt(30)
tommy.stamp()
tommy.goto(0, -75)
tommy.tilt(30)
tommy.stamp()
tommy.goto(-300, -50)
tommy.tilt(30)
tommy.stamp()
tommy.goto(300, 50)
tommy.tilt(30)
tommy.stamp()
tommy.goto(0, 75)
tommy.tilt(30)
tommy.stamp()
tommy.goto(-300, 50)
tommy.tilt(30)
tommy.stamp()
tommy.turtlesize(1);
tommy.home()

#Border of Flag
tommy.penup()
tommy.pensize(5)
tommy.color('black')
tommy.goto(350,200)
tommy.pendown()
tommy.goto(350,-200)
tommy.goto(-350,-200)
tommy.goto(-350,200)
tommy.goto(350,200)
tommy.penup()
tommy.home()

# Text
tommy.color('yellow')
tommy.goto(5, -27)
tommy.write("FLAG OF TURTLE-LOVERS", align="center", font=('Brush Script MT', 32, "bold"))

tommy.color('black')
tommy.goto(0, -25)
tommy.write("FLAG OF TURTLE-LOVERS", align="center", font=('Brush Script MT', 32, "bold"))


tommy.home()
tommy.hideturtle()
