def F(n):
    p=""
    while n > 0:
        p+=str(n%5)
        n//=5
    return p

for i in range(4,1000):
    num=F(i)
    if i%25==0:
        num=str(int(num)%1000)+num
    else:
        ost=i%25
        num+=F(ost)
    b=int(num, 5)
    if b>10000:
        print(i)
        break