# Особые числа = отриц числа, оканч на 4.
# Найти max сумму под-ти, в которой кол-во особых % 7, а сумма % 25
f = open("../27_1.txt")
n = int(f.readline())
a = [int(x) for x in f]
m = []  # Лучше брать пустой СПИСОК, потому что есть отрицательные числа!
for i in range(n):
    s = 0
    k = 0  # Количество особых чисел
    for j in range(i, n):
        s += a[j]
        if a[j] < 0 and str(a[j])[-1] == "4":
            k += 1
        if k % 7 == 0 and s % 25 == 0:
            m.append(s)
print(max(m))
