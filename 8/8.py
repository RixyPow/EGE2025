from itertools import product
k=0
for i in product('01234567', repeat=4):
    s=''.join(i)
    if s.count('6')==1 and int(s[0])%2!=0:
        k+=1
print(k)