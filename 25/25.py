k=0 #колво
x=860001 #числа
while k<5:
    M=0 #разность max и min
    for i in range(2, x//2+1):
        if x%i==0:
            M=x//i-i
            break
    if M!=0 and M%100==18:
        k+=1
        print(x, M)
    x+=1