# Цепочка из всех буквы - найти max строку без D
f = open("../Файлы/k7a-4.txt")
s = f.readline().split("D")
print(len(max(s, key=len)))