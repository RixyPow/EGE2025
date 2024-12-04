from turtle import *
k=30
tracer(0)
pensize(5)
left(90)
right(45)
for i in range(7):
    forward(5*k)
    right(45)
    forward(10*k)
    right(135)
up()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x*k, y*k)
        dot(5)
done()
