from ipaddress import *
for mask in range(33):
    net1=ip_network(f'132.214.105.51/{mask}', 0)
    if net1.network_address==ip_address('132.214.105.0'):
        print(mask)
