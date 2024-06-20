import turtle
import time


# Set up the screen
wn = turtle.Screen()
wn.title("Graphics test")
wn.bgcolor("white")

#writer
my_turtle = turtle.Turtle()
my_turtle.color("black")
my_turtle.shape("turtle")
my_turtle.hideturtle()
my_turtle.penup()
my_turtle.speed(1)


#wheeere
my_turtle.goto(0,0)


#the thing writing
my_turtle.write("Hello, World!", align="center", font=("Arial", 24, "normal"))


time.sleep(2)

my_turtle.clear()
my_turtle.write("Test 123", align="center", font=("Arial", 24, "normal"))


time.sleep(2)


a = 0
for _ in range(10):
 my_turtle.clear()
 my_turtle.write(a, align="center", font=("Arial", 24, "normal"))
 time.sleep(0.1)
 a = a + 1
 
time.sleep(1)

wn.bgcolor("black")
my_turtle.color("white")

my_turtle.write("Click to end", align="center", font=("Arial", 30, "bold"))







# Close the window when clicked
wn.exitonclick()