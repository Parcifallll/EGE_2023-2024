# Найти количество непрерывных под-стей, сумма элементов % 67 = 0
f = open("../27_1.txt")
n = int(f.readline())
count = 0
a = [int(x) for x in f]
for i in range(n):
    s = []  # можно списком, либо s = 0
    for j in range(i, n):
        s.append(a[j])
        if sum(s) % 67 == 0:
            count += 1
print(count)
