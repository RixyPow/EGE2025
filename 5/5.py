k=0
for i in range(30000000, 50000000):
    b=bin(i)[2:]
    b=b+2*str(bin(i%3)[2:])
    b=b+(bin(int(b, 2)%5)[2:])*3
    if int(b,2) in range(1222222222, 1555555667):
        k+=1
print(k)
