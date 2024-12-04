from turtle import *
k=25
tracer(0)
pensize(1)
left(90)
speed(100)
right(90)
for i in range(3):
    right(45)
    forward(10*k)
    right(45)
right(315)
forward(10*k)
for i in range(2):
    right(90)
    forward(10*k)
up()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x*k, y*k)
        dot(5)
done()
