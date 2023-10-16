f = open("Файлы ЕГЭ 2023-2024/17_1.txt")
a = [int(i) for i in f]
aver = sum(a) / len(a)
pairs = []
for i in range(len(a) - 1):
    x, y = a[i], a[i + 1]
    if abs(x-y) <= 20 and x + y > aver:
        pairs.append(x + y)
print(len(pairs), max(pairs))