def Del(n, m):
    if n % m == 0:
        return True
    else:
        return False


for A in range(1, 101):
    k=0
    for x in range(1, 101):
        if ((not(Del(x, A))) <= (Del(x, 6) <= (not(Del(x, 9)))))==True:
            k+=1
    if k==10000:
        print(A)
