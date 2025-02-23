from ipaddress import *
k=0
h=[]
net=ip_network('218.194.82.148/255.255.255.192', 0)
for ip in net:
    k+=1
    h.append(ip)
    print(k, max(h))
    