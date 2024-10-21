from ipaddress import *
net=ip_network(f'64.128.194.208/255.255.224.0', 0)
print(net.network_address)