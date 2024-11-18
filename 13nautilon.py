from ipaddress import *
k=0
net=ip_network('', 0)
for ip in net:
    bip=f'{ip:b}'
    if bip.count('1')%2==0:
        k+=1
print(k)