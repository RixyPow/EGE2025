a=350001
k=0
while k<6:
    p=0
    for d1 in range(2, a//2+1):
        if a%d1==0:
            p = a//d1
            break
    sp=[]
    for d2 in range(2, p//-1):
        if p%d2==0:
            break
        else:
            print(a, p)
            k+=1
    a+=1