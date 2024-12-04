from ipaddress import *
for mask in range(33):
    net1=ip_network(f'202.3.20.24/{mask}', 0)
    net2 = ip_network(f'202.3.27.11/{mask}', 0)
    if net1.network_address==net2.network_address:
        print(net1.netmask)