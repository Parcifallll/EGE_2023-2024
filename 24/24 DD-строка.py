#Дана строка из A B C D E F. DD-строка = D...D (граничные входят, строка НЕ пустая). Найти min DD-строку
f = open("24-153.txt")
s = f.readline().split("D")
a = min(len(i) for i in s if len(i) != 0) + 2 # +2 Потому что прибавляем D и D
print(a)