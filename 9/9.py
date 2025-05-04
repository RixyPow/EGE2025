with open('9fev54564.txt') as f:
    k=0
    for s in f:
        a=sorted(int(x) for x in s.split())
        povt=[y for y in a if a.count(y)>1]
        nepovt=[y for y in a if a.count(y)==1]
        if len(povt)==3 and (sum(povt)**2 > sum(nepovt)**2):
            k+=1
    print(k)
