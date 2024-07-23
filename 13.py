from ipaddress import *
for mask in range(33):
    net=ip_network(f'20.24.110.42/{mask}', 0)
    if net.network_address==ip_address('20.24.96.0'):
        print(bin(mask))