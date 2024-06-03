#6608 Места на футбольный матч
f = open("../Файлы/26-124.txt")
k, m, n = map(int, f.readline().split())
a = [int(x) for x in f]
a.sort(reverse=1)
places = [m] * k
count = 0
for i in range(n):
    offer = a[i]
    for j in range(k):
        if places[j] >= offer:
            places[j] -= offer
            count += 1
            break
print(count, sum(places))
