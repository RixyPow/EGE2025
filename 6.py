from turtle import *
k=35
tracer(0, 0)
pensize(5)
left(90)
speed(100)
for p in range(5):
    forward(9*k)
    right(90)
    forward(3*k)
    right(90)
up()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x*k, y*k)
        dot(5)
done()
