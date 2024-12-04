import math
k=[]
for n in range(1, 100):
    for m in range(1, 100):
        a=3*n+4*m
        if (m+2*n)>40 and (math.factorial(a-1)+1)%a==0:
            k.append(m+2*n)
print(min(k))
