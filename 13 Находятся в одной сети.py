#Два УЗЛА находятся в одной сети. Даны их IP-адреса. Укажите наиб возможное значение третьего слева байта маски сети
from ipaddress import *
ip1 = ip_address('112.117.107.70')
ip2 = ip_address('112.117.121.80')
for mask in range(33):
    net1 = ip_network(f'{ip1}/{mask}', 0)
    net2 = ip_network(f'{ip2}/{mask}', 0)
    if net1 == net2:
        print(net1.netmask)
