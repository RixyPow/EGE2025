with open('9.today.txt') as f:
    k=0
    for s in f:
        a=sorted(int(x) for x in s.split())
        povt=[x for x in a if a.count(x)==2]
        nepovt=[y for y in a if a.count(y)==1]
        if len(povt)==2 and bin(sum(povt))[2:].count('1') > bin(sum(nepovt))[2:].count('1'):
            k+=1
    print(k)