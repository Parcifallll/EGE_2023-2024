#6406
f = open("../Файлы/26-119.txt")
n, l, m = map(int, f.readline().split())
a = []
for i in range(n):
    st, r, t = f.readline().split()  # Начало стоянки, окончание стоянки, тип авто
    a.append([int(st), int(st) + int(r), t])
a.sort()
bus = 0
cnt = 0
park = [0] * (l + m)  # ВСЕ места
for i in range(n):  # Для каждой машины
    st, end, t = a[i]
    if t == "A":  # Если машина - паркуем на А или В!
        for j in range(l + m):  # для каждой парковки
            if park[j] <= st:
                park[j] = end
                break
        else:  # Если НИ одна парковка не подошла
            cnt += 1
    if t == "B":
        for j in range(l, l + m):  # Для парковок типа М
            if park[j] <= st:
                park[j] = end
                bus += 1
                break
        else:  # Если НИ одна парковка не подошла
            cnt += 1
print(bus, cnt)
