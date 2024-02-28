# Чуть более распространенное решение через цикл for else
#Функцию ДЕЛ() лучше не переписывать!
def f(A, x): return ((x % 34 == 0) and (x % 51 != 0)) <= ((x % A != 0) or (x % 51 == 0))


for A in range(1, 10000):
    for x in range(1, 10000):
        if f(A, x) == 0:
            break
    else:
        print(A)  # Ищем минимальный А
        break
