
f = open("Файлы/1.txt")
a = [int(i) for i in f]
max_n = max(int(i) for i in a if str(i)[-1] == "3") ** 2  # кв макс оканч на 3
pairs = []
for i in range(len(a) - 1):
    x, y = a[i], a[i + 1]  # только одно число оканч на 3
    if (str(x)[-1] == "3") + (str(y)[-1] == "3") == 1 and (x ** 2 + y ** 2) >= max_n:
        pairs.append(x ** 2 + y ** 2)
print(len(pairs), max(pairs))
