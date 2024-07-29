import turtle as t
k=15 #размер
t.left(90)
t.speed(100)
t.tracer(0,0)
t.pensize(2)

for n in range(5, 6):
    t.forward((n+2)*k)
    for i in range(4):
        t.forward(n*k)
        t.right(90)
        t.forward((n+2)*k)
    t.right(90)
    t.forward(2*n*k)
    for i in range(4):
        t.right(90)
        t.forward((3*n-1)*k)

for x in range(-30, 30):
    for y in range(-30, 30):
        t.up()
        t.goto(x*k, y*k)
        t.dot(5)
t.done()
