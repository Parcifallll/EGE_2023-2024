# Сколькими способами можно поставить в соответствие переменные?
from itertools import product, permutations


def f(x, y, z, w):
    return (x and (y <= z)) or w


d = set()  # сюда будем сохранять полученные перестановки
for a1, a2, a3, a4, a5, a6 in product([0, 1], repeat=6):
    table = [(1, 0, a1, 1), (a2, 0, 1, a3), (a4, 0, a5, a6)]
    for p in permutations("xyzw"):
        if [f(**dict(zip(p, row))) for row in table] == [0,0,0]:
            d.add(p)
print(len(d))
