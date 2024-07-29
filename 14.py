k=[]
s = abs(18 * 7**108 - 5 * 49**76 + 343**35 - 50)
print(s)
p = ""

while s > 0:
    k.append(s%49)
    s //= 49
print(k)
print(sum(k))
