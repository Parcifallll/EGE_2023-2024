#Без сочетания KEGE
s = open("../Файлы/24-157.txt").readline().replace("KEGE", "KEG EGE").split()
print(max(len(i) for i in s))