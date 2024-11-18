from itertools import product
k=0
h=[]
for i in product('01234567', repeat=5):
    s=''.join(i)
    k+=1
    if s.count('1')<=1:
        h.append(k)
print(len(h))