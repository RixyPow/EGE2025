from itertools import product
h=[]
for i in product('НРТУ', repeat=4):
    s=''.join(i)
    h.append(s)
print(h[214])