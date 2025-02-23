from turtle import *
k=25
tracer(0)
pensize(1)
left(90)
speed(100)
right(90)
for i in range(5):
    forward(7*k)
    right(120)
up()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x*k, y*k)
        dot(5)
done()
