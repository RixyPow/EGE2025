def F(n):
    b = ''
    while n > 0:
        b = str(n%3)+b
        n //= 3
    return b
h=[]
for i in range(5, 1000):
    q=F(i)
    if i % 3==0:
        q=q+q[-2]+q[-1]
    else:
        k=0
        for c in q:
            k+=int(c)
        q=q+F(k)
    if int(q,3)>=220:
        h.append(int(q,3))
print(min(h))


