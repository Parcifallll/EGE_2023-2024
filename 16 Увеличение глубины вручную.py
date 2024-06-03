from functools import lru_cache


@lru_cache
def f(n):
    if n == 1: return 1
    if n > 1 and n % 2 == 0: return n // 2 + f(n - 1)
    if n > 1 and n % 2 != 0: return n + f(n - 2)


for n in range(2, 10000):
    f(n)  # Просто вызываем функцию и сохраняем в память ее значение - заполняем кэш значениями для f
print(f(10000) - f(9993))
# Переписали sys.setrecursionlimit() - и даже гораздо лучше!
