from itertools import *
k=0
for i in product('АНДРЕЙ', repeat=7):
    s=''.join(i)
    if s.count('А')==1 and s.count('Й')==1 and s[0]!='Й':
        k+=1
print(k)

