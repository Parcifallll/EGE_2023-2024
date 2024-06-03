#Максимальное кол-во идущих подряд пар ZX ИЛИ ZY. Остальное заменяем на пробелы.
s = open("../Файлы/24-196.txt").readline()
s = s.replace("ZX", "*").replace("ZY", "*")
s = s.replace("X", " ").replace("Y", " ").replace("Z", " ")
print(max(len(i) for i in s.split()))
#ВАЖНО: пересечений букв НЕТ! Иначе такое не пройдет!
