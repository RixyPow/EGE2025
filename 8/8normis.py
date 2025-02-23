from itertools import product
k=0
for i in product(range(0,13), repeat=7):
    if i[0]!=0 and str(i).count('5')>=2:
        z=0
        for j in range(len(i)-1):
            if (i[j]%2)==(i[j+1]%2):
                z+=1
        if z==0:
            k+=1
print(k)

