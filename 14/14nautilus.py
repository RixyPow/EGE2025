s=9**18 + 3**54 - 9
k=0
while s>0:
    if s%3==2:
        k+=1
    s//=3
print(k)