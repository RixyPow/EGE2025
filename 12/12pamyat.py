from itertools import product
k=[]
for i in product('12', repeat=20):
    s='0'+''.join(i) +'0'
    if s.count('1')==10 and s.count('2')==10:
        while '00' not in s:
            s.replace('012', '30', 1)
            if '011' in s:
                s=s.replace('011', '20', 1)
                s = s.replace('022', '40', 1)
            else:
                s = s.replace('01', '10', 1)
                s = s.replace('02', '101', 1)
        if s.count('1')==6 and s.count('2')==5:
            k.append(s.count('4'))
print(max(k))