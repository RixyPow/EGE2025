
s = abs(18 * 7**108 - 5 * 49**76 + 343**35 - 50)
print(s)
p = ""

while s > 0:
    p = str(s % 49) + p
    s //= 49
print(p)
summa = sum(int(i) for i in p)
print(summa)
