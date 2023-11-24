#Определите min значение n и их сумму, при котором sum выведенных чисел f(n) > 5_000_000?
def f(n):
    global cnt
    #print("*")
    cnt += 2 * n + 1
    if n > 1:
        # print("*")
        cnt += 3 * n - 8
        f(n - 1)
        f(n - 4)
# Если такой метод не работает -> преобразуем в рекуррентную формулу

n = 0
while True:
    n += 1
    cnt = 0
    f(n)
    if cnt > 5_000_000:
        print(n, cnt)
        break
