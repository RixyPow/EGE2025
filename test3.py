k=0
for a in range(2, 100):
    k+=9+(a-2)*10
    print(a, k)
    if k>1000:
        break