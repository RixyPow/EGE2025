from ipaddress import *
net = ip_network('122.159.136.144/255.255.255.248', 0)
cnt=0
for ip in net:
    s = f'{ip:b}'
    if s.count('1')%4 != 0:
        cnt+=1
    print(cnt)
