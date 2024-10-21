from itertools import product
h=[]
for i in product('ВНРТ', repeat=4):
    s=''.join(i)
    h.append(s)
print(h[249])