# A - y==15
# B - y<0 x>0 else

clusterA=[[], []]
clusterB=[[], [], []]

for s in open('27var1Anorm.txt'):
    x,y=[float(c) for c in s.split()]
    if y>15:
        clusterA[0].append([x,y])
    else:
        clusterA[1].append([x, y])
for s in open('27var1Bnorm.txt'):
    x, y = [float(c) for c in s.split()]
    if y<0:
        clusterB[0].append([x,y])
    elif x>0:
        clusterB[1].append([x, y])
    else:
        clusterB[2].append([x, y])

from math import dist
def centr(klas):
    k=[]
    for i in klas:
        sm=sum(dist(i,i1) for i1 in klas)
        k.append([sm, i])
    return min(k)[1]
centroidA=[centr(klas) for klas in clusterA]
centroidB=[centr(klas) for klas in clusterB]

PxA=sum([x for x,y in centroidA])/2
PyA=sum([y for x,y in centroidA])/2

PxB=sum([x for x,y in centroidB])/3
PyB=sum([y for x,y in centroidB])/3

print(abs(int(PxA*10000)), abs(int(PyA*10000)))
print(abs(int(PxB*10000)), abs(int(PyB*10000)))