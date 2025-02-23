def F(x, y):
    if x<y or x==5:
        return 0
    elif x==y:
        return 1
    elif x>y:
        return F(x-1, y) + F(x-3, y) + F(x//3, y)
print(F(29,12)*F(12,3))