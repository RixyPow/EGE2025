k=[]
for A in range(0,300):
    F=True
    for x in range(1,300):
        for y in range(1,300):
            if (((x<6)<=(x**2<A)) and ((y**2<A) <= (y<=6))) == False:
                F=False
                break
    if F==True:
        k.append(A)
print(len(k))