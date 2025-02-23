with open('../9hw3.txt') as f:
    k=0
    for s in f:
        a=sorted(int(x) for x in s.split())
        povt=[y for y in a if a.count(y)==2]
        nepovt = [y for y in a if a.count(y) ==1]
        if len(povt)==4 and len(nepovt)==3 and sum(nepovt)/3 < sum(povt)/4:
            k+=1
    print(k)