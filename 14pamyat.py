s=4**2014+2**2015-8
b=bin(s)[2:]
k=0
for i in b:
    k+=int(i)
print(k)