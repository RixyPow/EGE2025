from ipaddress import *
for bik in range(33):
    net1=ip_network(f'{bik}/255.255.255.192', 0)
    if net1.network_address=='10.18.134.220':
        print(net1.netmask)