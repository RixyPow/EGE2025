def Del(n, m):
    if n % m == 0:
        return True
    else:
        return False


for A in range(1, 151):
    k=0
    for x in range(1, 151):
        for y in range(1, 151):
            if (Del(108, x) <= (not (Del(x, y)))) or (x + y > 80) or (A - y > x):
                k += 1
    if k==     22500:
        print(A,k)
