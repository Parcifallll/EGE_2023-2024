import sys
from functools import lru_cache

sys.setrecursionlimit(10000)  # Расширяем глубину рекурсии (мах =  10000)


@lru_cache  # Декоратор, подменяет нашу функцию на кэшированную функцию
def F(n):
    if n <= 2:
        return 1
    if n > 2:
        return G(n - 2)


@lru_cache
def G(n):
    if n <= 1:
        return 1
    if n > 1:
        return F(n - 1) + n + 1


print(F(8))
