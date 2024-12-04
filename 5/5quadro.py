def F(ch):
    q=''
    while ch>0:
        q=str(i%3)+q
        ch//=3
    return q
for i in range(0,1000):
    norm=F(i)
    if i%3==0:
        norm='1'+norm+'02'
    else:
        norm=norm+str(F(i%3*4))
    if int(norm, 3)<199:
        print(i)
