k=[]
for n in range(33, 1000):
    b=bin(n)[2:]
    if n%2==1:
        b='1'+b[:-2]+'10'
    else:
        b='10' + b[2:0] +'1'
    k.append(int(b, 2))
print(min(k))
