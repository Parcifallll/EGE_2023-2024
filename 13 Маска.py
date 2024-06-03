from ipaddress import *

for mask in range(33):  # Перебираем маску - набор единиц
    net = ip_network(f'124.32.48.131/{mask}', 0)
    if net.network_address == ip_address('124.32.32.0'):  # Если текущий адрес сети равен заданному - это искомая маска. ip_address - Создание ТИПА адреса (type address)
        print(net.netmask)  # Печатаем маску (в десятичном виде)
        print(net)  # Печатаем маску (кол-во единиц)
