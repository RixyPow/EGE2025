from ipaddress import *
net=ip_network(f'32.64.208.224/255.255.192.0', 0)
print(net.network_address)