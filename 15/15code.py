for A in range(1,300):
    F=True
    for x in range(1,300):
        for y in range(1,300):
            if ((x-3*y<A) or (y>400) or (x>56))==False:
                F=False
                break
    if F==True:
        print(A)
        break