# Выбрать такую подпоследовательность подряд идущих чисел, чтобы сумма была max и % 10 == 0
f = open("../27_1.txt")
n = int(f.readline())
a = [int(x) for x in f]
m = 0
for i in range(n):
    s = 0  # Сумма элементов
    for j in range(i, n):  # Теперь цикл начинается с i !!! (в парах было i+1)
        s += a[j]
        print(s)
        if s % 10 == 0:
            m = max(m, s)
print(m)
