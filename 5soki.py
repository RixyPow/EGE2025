for i in range(7, 100):
    n=str(bin(i)[2:])
    perevorot=''
    for j in n:
        perevorot=j+perevorot
    if int(perevorot, 2) == 13:
        print(i)
