with open('9ya4.txt') as f:
    k=0
    for s in f:
        a=sorted(int(x) for x in s.split())
        ch=[y for y in a if y%2==0]
        nech = [y for y in a if y % 2 == 1]
        z=1
        for j in ch:
            z=z*j
        if len(ch)>=2 and len(nech)>=2 and 3*sum(nech)>z:
            k+=1
    print(k)