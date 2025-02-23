def F(n):
    if n == 1:
        return 1
    elif n==2:
        return 1
    else:
        return F(n-2) * n
print(F(6))