# Рассматриваются пары элементов, расположенных на расстоянии не менее 8. Найти кол-во пар, разность в которых кратна 999
# Расстояние = разница в индексах
f = open("../Файлы/27-2.txt")
n = int(f.readline())
a = [int(x) for x in f]
count = 0
for i in range(n):
    for j in range(i + 1, n):
        if (j - i) >= 8 and (a[i] - a[j]) % 999 == 0:
            count += 1
print(count)
