
for a in range(-300,300):
    F=True
    for x in range(1,300):
        for y in range(1,300):
            if ( -((x-2)**2) + 3 < y or ((x-1)**2+(y**2)<7) or (5*x+a) > y)==False:
                F=False
    if F==True:
        print(a)
        break