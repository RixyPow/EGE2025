def F(ch):
    q=''
    while ch>0:
        q=str(i%2)+q
        ch//=2
    return q
for i in range(16,1000):
    norm=F(i)
    if i%3==0:
        norm=norm+norm[-3]+norm[-2]+norm[-1]
    else:
        norm=norm+str(F(i%3*3))
    if int(norm, 2)>=76:
        print(i)
