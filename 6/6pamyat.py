from turtle  import *
tracer(0)
k=35
pensize(5)
left(90)
for i in range(3):
    forward(7*k)
    right(90)
forward(10*k)
for i in range(3):
    left(90)
    forward(6*k)
up()
for x in range(-30, 30):
    for y in range(-30, 30):
        setpos(x*k, y*k)
        dot(10)
done()