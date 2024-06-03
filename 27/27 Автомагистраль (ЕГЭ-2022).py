# На каждом километре автомагистрали, начиная с первого, расположены пункты питания.
# По правилам готовую еду нельзя перевозить на расстояние, превышающее М км.
# Для транспортировки используются термоконтейнеры вместимостью не более 6 готовых обедов.
# Каждый термоконтейнер используется для доставки только в один пункт питания
# Компания расположила 1 пункте питания цех для производства готовых обедов
# Определите необходимое суммарное количество термоконтейнеров для ежедневной перевозки готовых обедов в пункты питания из этого цеха
f = open()
n, m = map(int, f.readline().split())
a = []
mx = 0
for i in range(n):
    if i % 6 == 0:
        a[i] = i // 6  # Если кол-во контейнеров целое
    else:
        a[i] = (i // 6) + 1  # Если не целое то +1 контейнер

    # Проверяем различное расположение цехов
for i in range(n):
    s = 0
    for j in range(n):
        if abs(i - j) <= m:  # Если расстояние подходит
            s += a[j]
    mx = max(mx, s)
print(m)
