def F(n):
    if n < 2:
        return 2
    elif n>=2 and n%2==0:
        return F(n//2)+1
    elif n>=2 and n%2==1:
        return F(3*n+1)+1
k=0
for i in range(1, 100001):
    if F(i)==16:
        k+=1
print(k)