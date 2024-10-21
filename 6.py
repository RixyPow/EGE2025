from turtle import *
k=35
tracer(0, 0)
pensize(5)
left(90)
speed(100)
for i in range(4):
    forward(8*k)
    right(90)
    forward(8 * k)
    right(30)
up()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x*k, y*k)
        dot(5)
done()
