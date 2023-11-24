# Дин-прог СВЕРХУ является рекурсией с кэшированием

cache = [None] * 1000  # Недостаток - может не хватить места


def Fibonacci(n):
    if cache[n] != None:
        return cache[n]  # т.е. мы уже считали это значение
    elif n == 1 or n == 0:
        return n  # крайние случаи
    else:
        result = Fibonacci(n - 1) + Fibonacci(n - 2)
    cache[n] = result  # сохраняем значение
    return result


print(Fibonacci(10))
