from itertools import combinations
#Найти макс/мин четную сумму пары
f = open(r"/27_1.txt")
n = int(f.readline())
a = [int(x) for x in f]
p = []
for x, y in combinations(a, 2):
    if (x + y) % 2 == 0:
        p.append(x + y)
print(max(p), min(p))