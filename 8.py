from itertools import product
k=0
h=[]
for i in product('АГИЛМНОФ', repeat=5):
    s=''.join(i)
    k+=1
    if s[0]!='Н' and s.count('О')<=1 and k%2==1:
        h.append(k)
print(len(h))