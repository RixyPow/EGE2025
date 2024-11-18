k=[]
for i in range(50000000,60000000):
    h=[]
    for d in range(2, i//2+1):
        if i%d==0:
            h.append(d)
    if len(h)==6 and 911 in h:
        k.append(i)
print(len(k), min(k))
