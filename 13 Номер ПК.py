#Дана маска и IP-адрес, найти номер ПК
from ipaddress import *
net = ip_network(f'206.158.124.67/255.255.224.0', 0) #Передаем IP-адрес
k = 0
for ad in net: #Перебираем все ip-адреса в данной сети
    k += 1 #Увеличиваем номер ПК
    if ad == ip_address('206.158.124.67'):
        print(k)
        break