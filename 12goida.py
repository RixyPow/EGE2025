for n in range(3,1000):
        s='3'+n*'5'
        while '25' in s or '355' in s or '555' in s:
                s=s.replace('25', '3', 1)
                s=s.replace('355', '52', 1)
                s=s.replace('555', '23', 1)
        k=0
        for i in s:
                k+=int(i)
        if k==27:
                print(n)
