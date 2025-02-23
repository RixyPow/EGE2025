from turtle import *
k=30
tracer(0)
pensize(0.5)
left(90)
for i in range(42):
    right(60)
    forward(7*k)
    right(60)
up()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x*k, y*k)
        dot(2)
done()
