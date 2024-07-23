n=int(input()) #число
k=int(input()) #cc
s=''
while n>0:
    s=str(n%k)+s
    n//=k
print(s)