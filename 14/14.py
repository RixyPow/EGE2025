mx=0
maxx=0
h=[]
for x in range(2, 2026):
    k=0
    s=5**2025+5**200-x
    while s>0:
        if s%5==4:
            k+=1
        s=s//5
    h.append(k)
    if k==199:
        print(x)
