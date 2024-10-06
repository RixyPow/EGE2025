from ipaddress import *
net=ip_network(f'84.77.95.123/255.255.224.0', 0)
print(net.network_address)