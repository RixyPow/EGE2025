from itertools import product
k=0
for i in product('АКРУ', repeat=5):
    s=''.join(i)
    k+=1
    if s=='УКАРА':
        print(k)