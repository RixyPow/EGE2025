from turtle import *
k=15
left(90)
speed(100)
tracer(0)
pensize(5)
cnt=0
for i in range(4):
    forward(14*k)
    right(90)
for i in range(5):
    forward(5*k)
    right(45)
canvas=getcanvas()

up()
for x in range(-30, 30):
    for y in range(-30, 30):
        item = canas.find_overlapping(x,y,x,y)
        if len(item)==1 and item[0]==5:
            cnt+=1
print(cnt)
done()