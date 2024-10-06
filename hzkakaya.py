def F(n):
    s=''
    while n>0:
        s=str(n%3)+s
        n//=3
    return s

for n in range(9,1000):
    s = F(n)
    if n%3==0:
        s+=s[-3]+s[-2]+s[-1]
    else:
        s+=(F(n%3*2))
    if int(s,3)>150:
        print(n, int(s,3), F(n))
        break


