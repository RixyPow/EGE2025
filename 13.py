from ipaddress import *
k=[]
for mask in range(33):
    net1=ip_network(f'119.83.200.27/{mask}', 0)
    if net1==ip_address('119.83.192.0'):
        k.append(net1)
print(k)