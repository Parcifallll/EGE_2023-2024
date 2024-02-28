def f(A, x, y):
    return (x + y <= 25) or (x <= y + 5) or (x >= A)


for A in range(1, 100):
    if all(f(A, x, y) for x in range(1, 100) for y in range(1, 100)):
        print(A)

# Если нет ответа - либо ошибка, либо НЕ хватило диапазона А и Х
