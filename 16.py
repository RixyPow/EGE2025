def F(n):
    if n>10000:
        return 42
    elif n%2==0:
        return 2*n + F(n+3) + F(n+4) + F(n+6)
    elif n%2==1:
        return -(n+F(n+1)+F(n+3))
print(F(9996)-F(9994))