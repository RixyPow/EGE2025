from itertools import product
k=0
for i in product('01234567', repeat=4):
    s=''.join(i)
    ch=int(s, 8)
    if s[0]!='0' and (((int(s[0])+int(s[1]))%2==1) and ((int(s[1])+int(s[2]))%2==1) and ((int(s[2])+int(s[3]))%2==1)) and ('111' not in (str(bin(ch)[2:]))):
        k+=1
print(k)
