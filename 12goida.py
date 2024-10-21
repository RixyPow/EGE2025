k=[]
h=[]
for n in range(100,10000):
        if n%9==0:
                s=n*'5'
                while '555' in s or '11' in s or '2' in s:
                        s=s.replace('555', '1', 1)
                        s=s.replace('11', '25', 1)
                        s=s.replace('2', '5', 1)
                k.append(n)
                h.append(int(s))

print(k)
print(h)
