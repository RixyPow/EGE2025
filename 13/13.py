from ipaddress import *
for mask in range(33):
    net1=ip_network(f'213.168.83.190/{mask}', 0)
    if net1.network_address==ip_address('213.168.64.0'):
        print(mask)