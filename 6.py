import turtle as t
k=15 #размер
t.left(90)
t.speed(100)
t.tracer(0,0)

t.right(60)
t.forward(4*k)
t.right(120)
for i in range(4):
    t.forward(3*k)
    t.right(240)
    t.forward(3*k)
    t.right(120)
t.forward(4*k)
t.right(90)
t.forward(8*3**0.5*k)
t.right(90)
t.forward(8*k)
t.up()

for x in range(-30, 30):
    for y in range(-30, 30):
        t.goto(x*k, y*k)
        t.dot(5)
t.done()
