from itertools import product
k=0
h=[]
for i in product('ЕКМОПРТЬ', repeat=5):
    s=''.join(i)
    k+=1
    if s.count('К')==0 and s.count('Р')==2:
        h.append(k)
print(max(h))