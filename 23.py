def F(x, y):
    if x > y or x==13:
        return 0
    if x == y:
        return 1
    else:
        return F(x+1, y) + F(x+2, y) + F(x*3, y)
print(F(3,8)*F(8,18))