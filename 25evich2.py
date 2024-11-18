def divs(x):
    k=2
    for i in range(2, int(x**0,5)+1):
        if x%i==0:
            k+=1
            if i!=x//i:
                k+=1
    return k
a=100
print(divs(a))