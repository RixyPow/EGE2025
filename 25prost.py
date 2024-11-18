k=0 #колво
x=550001 #числа
while k<6:
    for i in range(2, x//2+1):
        D=0
        if x%i==0:
            D=x//i
        if D!=0:
            for i2 in range(2, D//2+1):
                sp=[]
                if D%i2==0:
                    sp.append(i2)
            if len(sp)==0:
                k+=1
                print(x, D)
                break
    x+=1