f = open("../Файлы/26-76.txt")
l, n = map(int, f.readline().split())
day = [0] * (l + 1)
for i in range(n):
    st, end = map(int, f.readline().split())
    day[st] += 1
    day[end] -= 1
k = 0
c = m = s = 0
for i in range(l):
    k += day[i]
    if k == 0:
        c += 1
    else:
        m = max(m, c)
        s += c
        c = 0
    # Суммарная длительность простоев
print(s, m)
