# Дин прог -> Найти макс сумму идущих подряд убывающих чисел (почти 26-27 задачка)
file = open('data1.txt')
data = [int(x) for x in file] #Массив из последовательно-идущих чисел
maxsum = 0
s = data[0] #Первая сумма = первое число
for i in range(1, len(data)):
    s = data[i] + s * (data[i] < data[i - 1]) #Сумма = текущее число + предыдущее(если оно больше i-того)
    maxsum = max(maxsum, s)
print(maxsum)
