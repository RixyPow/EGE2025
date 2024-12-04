from itertools import product
h=[]
for i in product('012345678', repeat=12):
    s=''.join(i)
    k=0
    for j in range(len(s)):
        if int(j)%2==1:
            k+=1
    if k == 3:
        h.append(s)
    for k1 in h:
        for k2 in range(len(k1)-1):
            if int(k1[k2])%2==1 and int(k1[k2+1])==1:
                h.remove(k1)
print(len(h))