#Состоит из A, B, C, 1, 2, 3. Найти максимальное кол-во подряд троек буква+цифра+цифра
s = open("../Файлы/24-215.txt").readline()
s = s.replace("B", "A").replace("C", "A").replace("2", "1").replace("3","1")
s = s.replace("A11", "*").replace("A", " ").replace("1", " ")
print(max(len(i) for i in s.split()))
#Замена работает ТОЛЬКО без пересечений