### TOP LEVEL (defintions of functions and import statements)
# Importing turtle
import turtle as t
screen=t.Screen
t.bgcolor("lightblue")
t.speed(12)

# Choosing random color function
def random_color():
    import random
    colors = ["red","blue","green","yellow","violet","orange"]
    colorchoice = random.choice(colors)
    t.fillcolor(colorchoice)
    t.begin_fill()
    return

# SFU logo function 
def sfu_logo():
    t.pendown()
    t.color("white")
    style = ("Trebuchet MS", 80, "bold")
    t.write("SFU", font=style, align="center")
    return

# Sun function (function with parameter)
def sun(turtle, color, size):
    t.color(color)
    t.fillcolor(color)
    t.begin_fill()
    t.circle(size)
    t.end_fill()
    t.pendown()
    return

# Cloud (includes 3 for loops and includes function with parameter)
def cloud(turtle, color):
    t.pendown()
    t.speed(25)
    t.pencolor(color)
    t.fillcolor(color)
    t.begin_fill()
    t.forward(40)
    t.forward(5)

# 3 Void functions

### MAIN LEVEL (start of program)

# Shape of the house
t.pencolor("light yellow")
t.fillcolor("light yellow")
t.begin_fill()

t.penup()
t.right(90)
t.right(90)
t.pendown()


t.forward(300)
t.left(90)
t.forward(300)
t.left(90)
t.forward(600)
t.left(90)
t.forward(300)
t.left(90)
t.forward(600)
t.left(90)
t.forward(300)
t.end_fill()


# Garage
t.pencolor("light grey")
t.fillcolor("light grey")
t.begin_fill()

t.penup()
t.left(90)
t.forward(560)
t.left(90)
t.forward(175)
t.left(90)
t.forward(260)
t.left(90)
t.forward(175)
t.end_fill()

# Door
t.fillcolor("brown")
t.left(90)
t.forward(300)
t.pendown()
t.left(90)
t.forward(300)
t.left(90)
t.forward(600)
t.left(90)
t.forward(300)
t.left(90)
t.forward(45)
t.begin_fill()
t.left(90)
t.forward(115)
t.right(90)
t.forward(85)
t.right(90)
t.forward(115)
t.right(90)
t.forward(85)
t.end_fill()

t.right(180)
t.forward(85)
t.left(90)
t.forward(53)

# DOOR KNOB
t.penup()
t.forward(5)
t.left(90)
t.forward(15)
t.pendown()
t.pencolor("yellow")
t.fillcolor("yellow")
t.begin_fill()
t.pendown()
t.circle(7)
t.end_fill()

# Wood thing
t.penup()
t.pencolor("orange")
t.fillcolor("orange")
t.right(180)
t.forward(30)

t.begin_fill()
t.pendown()
t.right(90)
t.forward(58)
t.left(180)
t.forward(58)
t.right(90)
t.forward(120)
t.right(90)
t.forward(58)
t.right(90)
t.forward(120)
t.left(180)
t.end_fill()

t.forward(120)
t.left(90)
t.forward(58)
t.left(90)
t.forward(30)
t.right(90)
t.pendown()

# Flower 1
t.pencolor("green")
t.forward(20)

random_color()

t.circle(5)
t.forward(3)
t.right(90)
t.circle(5)
t.forward(3)
t.right(138)
t.circle(5)
t.end_fill()
t.penup()

# Flower 2
t.right(42)
t.forward(31)
t.left(90)

t.pendown()
t.forward(23)
t.right(180)
t.forward(20)

random_color()

t.circle(5)
t.forward(3)
t.right(90)
t.circle(5)
t.forward(3)
t.right(138)
t.circle(5)
t.end_fill()
t.penup()

# Flower 3
t.right(42)
t.forward(31)
t.left(90)

t.pendown()
t.forward(23)
t.right(180)
t.forward(20)

random_color()

t.circle(5)
t.forward(3)
t.right(90)
t.circle(5)
t.forward(3)
t.right(138)
t.circle(5)
t.end_fill()

# First window (round)
t.penup()
t.right(41)
t.forward(52) #62
t.right(90)
t.forward(180)
t.left(90)
t.forward(40)

t.pencolor("black")
t.pendown()

random_color()

t.circle(40)
t.end_fill()

# innerpart of this window
t.left(89)
t.forward(80)
t.right(180)
t.forward(40)
t.right(90)
t.forward(40)
t.left(180)
t.forward(80)

# Second window (square)
t.penup()
t.right(180)
t.forward(125)
t.right(90)
t.forward(100)
t.left(90)
t.pendown()

random_color()

t.forward(90)
t.left(90)
t.forward(90)
t.left(90)
t.forward(90)
t.left(90)
t.forward(90)
t.left(90)
t.end_fill()
t.forward(45)
t.left(90)
t.forward(90)
t.right(90)
t.forward(45)
t.right(90)
t.forward(45)
t.right(90)
t.forward(90)
t.left(180)
t.forward(90)

# Third window (rectangle)
t.penup()
t.left(90)
t.forward(45)
t.right(90)
t.forward(90)

t.pendown()

random_color()

t.forward(180)
t.left(90)
t.forward(75)
t.left(90)
t.forward(180)
t.left(90)
t.forward(75)
t.end_fill()

t.left(90)
t.forward(90)
t.left(90)
t.forward(75)
t.left(90)
t.forward(90)
t.left(90)
t.forward(40)
t.left(90)
t.forward(180)

t.penup()
t.forward(68)
t.left(90)
t.forward(56) 

# Roof
t.pencolor("dark red")
t.fillcolor("dark red")
t.begin_fill()

t.pendown()
t.right(90)
t.forward(100)

t.left(155)
t.forward(445)
t.left(50)
t.forward(445)
t.left(155)
t.forward(804) # 600
t.left(180)
t.forward(204)
t.end_fill()

# Chimney
t.pencolor("dark red")
t.fillcolor("dark red")
t.begin_fill()

t.pendown() 
t.right(90)
t.forward(97)

t.pendown()
t.forward(80)
t.right(90)
t.forward(70)

t.right(90)
t.forward(114)
t.end_fill()

t.penup()
t.forward(50)
t.left(90)
t.backward(255)
# SFU LOGO
sfu_logo()

# Details of garage door
t.penup()
t.color("black")
t.right(180)
t.forward(8)
t.left(90)
t.forward(175)

t.pendown()
t.left(90)
t.forward(260)

t.right(90)
t.penup()
t.forward(35)

t.pendown()
t.right(90)
t.forward(260)

t.left(90)
t.penup()
t.forward(35)

t.pendown()
t.left(90)
t.forward(260)

t.right(90)
t.penup()
t.forward(35)

t.pendown()
t.right(90)
t.forward(260)

t.penup()
t.forward(298)
t.right(90)
t.forward(588)

# Sun
sun(t,"Yellow",80)

t.penup()
t.right(90)
t.forward(90)
t.right(90)
t.forward(140)
t.left(90)

# Cloud
cloud(t, "White")

t.forward(40)
t.left(90)
t.forward(5)

for x in range (1, 15):
  t.left(10)
  t.forward(7)

t.left(220)
for y in range (1,18):
  t.left(10)
  t.forward(7)

t.left(220)
for z in range (1,15):
  t.left(10)
  t.forward(7)
  
t.forward(5)
t.left(100)
t.forward(200)
t.end_fill()
t.hideturtle()
