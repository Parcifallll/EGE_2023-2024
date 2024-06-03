from itertools import combinations

# Количество ПАР элементов, в которых пара делится на 17 и сумма четна
f = open(r"D:\PycharmProjects\ЕГЭ 2023-2024\Файлы\27_1.txt")
n = int(f.readline())
a = [int(x) for x in f]
count = 0
for i in range(n):
    for j in range(i + 1, n):
        if (a[i] + a[j]) % 2 == 0 and a[i] * a[j] % 17 == 0:
            count += 1
# Альтернатива:
for x, y in combinations(a, 2):
    if x * y % 17 == 0 and (x + y) % 2 == 0:
        count += 1
print(count)
#СТАТИЧЕСКОЕ решение