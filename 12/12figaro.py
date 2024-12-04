for a1 in range(30):
    for a2 in range(30):
        for a3 in range(30):
            k1=a1+a3
            k2=a1+a2+2*a3
            k3=a2+2*a3
            if k1==23 and k2==48 and k3==41:
                print(a1+a2+a3)