for n in range(1000):
    b=bin(n)[2:]
    summa=b.count('1')
    b=b+str(summa%2)
    summa = b.count('1')
    b = b + str(summa % 2)
    if int(b, 2)>125:
        print(n)
        break