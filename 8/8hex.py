from itertools import product
k=0
for i in product('0123456789ABCDEF', repeat=5):
    s=''.join(i)
    #if s.count('6')==2 and