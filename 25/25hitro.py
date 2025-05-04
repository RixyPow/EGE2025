def F(n):
    r=n%2+1
    for i in range(r+1, int(n**0.5)+1,r):
        if n%i==0: return False
    return True
start,end=35000000,40000000
for i in range(start, end+1):
    n=i
    while n%2==0: n//=2
    q=round(n**0.25)
    if n==q**4 and F(q):
        print(i)