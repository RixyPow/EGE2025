from itertools import product
h=[]
for i in product('БКФ', repeat=6):
    s=''.join(i)
    h.append(s)
print(h[341])