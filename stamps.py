# Aaron Gould
# Assignment 5A: Travel Stamps
# COP 2500
# Feb 14, 2023

# Star wars inspired design

import turtle
turtle.speed(8)

#Yellow Circle
turtle.fillcolor("#FFDE06")
turtle.begin_fill()
turtle.circle(77)
turtle.end_fill()

#black circle
turtle.fillcolor('black')
turtle.begin_fill()
turtle.circle(75)
turtle.end_fill()

# A symbol
turtle.left(120)
turtle.penup()
turtle.forward(115)
turtle.right(120)
turtle.forward(25)
turtle.pendown()
turtle.pensize(1.5)
turtle.color("#FFDE06")
turtle.forward(10)
turtle.right(70)
turtle.forward(60)
turtle.right(110)
turtle.forward(17)
turtle.right(65)
turtle.forward(13)
turtle.left(70)
turtle.forward(10)
turtle.left(70)
turtle.forward(12)
turtle.right(75)
turtle.forward(17)
turtle.right(110)
turtle.forward(47)
turtle.left(110)
turtle.forward(15)
turtle.right(90)
turtle.forward(13)
turtle.right(90)
turtle.forward(25)
turtle.end_fill()

# A triangle
turtle.right(90)
turtle.penup()
turtle.forward(15)
turtle.left(70)
turtle.pendown()
turtle.right(40)
turtle.forward(15)
turtle.right(120)
turtle.forward(15)
turtle.right(120)
turtle.forward(15)

# G position
turtle.penup()
turtle.right(90)
turtle.forward(82)
turtle.right(140)
turtle.backward(5)

# G symbol
turtle.pendown()
turtle.right(5)
turtle.forward(17)
for i in range(16):
    turtle.forward(7.5)
    turtle.right(14)
turtle.right(90)
turtle.forward(15)
turtle.right(80)
for i in range(10):
    turtle.forward(5)
    turtle.left(20)
turtle.forward(10)
turtle.left(100)
turtle.forward(15)
turtle.right(90)
turtle.forward(20)
turtle.right(90)
turtle.forward(32)

# position pen for stars

turtle.penup()
turtle.right(45)
turtle.forward(50)
turtle.left(170)
turtle.pendown()

# Space stars
# Blue 
for size in range (70, 0, -1):
    turtle.pensize(size)
    turtle.pencolor('blue')
    turtle.dot(2.1)
    turtle.left(40)
    turtle.penup()
    turtle.forward(50 + size)
    turtle.pendown()
    turtle.left(90)
# Silver
for size in range (40, 0, -1):
    turtle.pensize(size)
    turtle.pencolor('silver')
    turtle.dot(2.2)
    turtle.left(40)
    turtle.penup()
    turtle.forward(50 + size)
    turtle.pendown()
    turtle.left(90)
# Red
for size in range (55, 0, -1):
    turtle.pensize(size)
    turtle.pencolor('red')
    turtle.dot(2.2)
    turtle.left(40)
    turtle.penup()
    turtle.forward(50 + size)
    turtle.pendown()
    turtle.left(90)
# Pen gtfo
turtle.penup()
turtle.forward(200)
turtle.pendown()
