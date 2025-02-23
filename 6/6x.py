from turtle import *
k=25
pensize(5)
tracer(0)
left(90)
a=6 #
for i in range(4):
    forward(a*k)
    right(90)
    forward(a*k)
    left(90)
    forward(a*k)
    right(90)
up()
for x in range(-30, 30):
    for y in range(-30, 30):
        setpos(x*k, y*k)
        dot(10)
done()