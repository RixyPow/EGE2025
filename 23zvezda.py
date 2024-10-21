def F(x, y):
    if x > y:
        return 0
    elif x == y:
        return 1
    elif x < y and x%2==1:
        return F(x+1, y) + F(x*2, y)+ F(x+1, y)
    elif x < y and x % 2 == 0:
        return F(x + 1, y) + F(x * 2, y) + F(x + 2, y)
print(F(3,9)*F(9,17) * F(17,25))