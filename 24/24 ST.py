#Макс подцепочка БЕЗ сочетания ST. То есть, строки АВВS TRD допустимы. Вставляем между ними пробел
s = open("Файлы/24_9791.txt").readline().replace("ST", "S T").split() #
print(max(len(i) for i in s))
