def F(n):
    global cnt
    cnt += 1
    if n >= 1:
        cnt += 1
        F(n - 1)
        F(n - 2)


cnt = 0
F(28)
print(cnt)
# Плохое решение(в продакшене за такое руки оторвут), лучше преобразовать в обычную математическую