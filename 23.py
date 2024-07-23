def F(x, y):
    if x > y or x == 81:
        return 0
    if x == y:
        return 1
    else:
        return F(x+x//10, y) + F(x+3, y) + F(2*x-1, y)
print(F(42,73)*F(73,89))