def F(x, y):
    if x > y or x==11:
        return 0
    elif x==y:
        return 1
    elif x < y:
        return F(x+1, y) + F(x+5, y) + F(x*2, y)
print(F(1, 9) * F(9, 18))