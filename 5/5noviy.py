def F(n):
    s=''
    while n>0:
        s=str(n%4)+s
        n//=4
    return s
k=[]
for i in range(2,10000):
    b=F(i)
    if len(b)%2==0:
        b=b[:(len(b)//2)]+'0'+b[(len(b)//2):]
    else:
        b=b+str(int(b[-1])%2)
    if int(b, 4) in range(100,151):
        k.append(int(b, 4))
print(k)