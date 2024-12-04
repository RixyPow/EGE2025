def F(n):
    b=''
    while n>0:
        b=str(n%3)+b
        n//=3
    return b
for n in range(1,1000):
    ch=F(n)
    if n%3!=0:
        ch=ch+str(F(n%3*5))
    if int(ch, 3)>146:
        print(n)