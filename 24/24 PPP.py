#Нет сочетания PPP - но replace не умеет обрабатывать "пересечения"
s = open("../Файлы/24-157.txt").readline()
while "PPP" in s:
    s = s.replace("PPP", "PP PP")
print(max(len(i) for i in s.split()))
