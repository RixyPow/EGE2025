k=[]
for n in range(128, 256):
    s=bin(n)[2:]
    s=s.replace('0', '#')
    s=s.replace('1', '0')
    s=s.replace('#', '1')
    a=int(s,2)
    if (n-a)==105:
        k.append(n)
print(k)
