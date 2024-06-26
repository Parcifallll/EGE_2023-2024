# Среди целых чисел, принадлежащих числовому отрезку [125697; 125721], найдите числа, которые представляют собой произведение двух различных простых делителей.
# Для каждого найденного числа запишите эти два делителя в таблицу на экране с новой строки в порядке возрастания произведения этих двух делителей.
# Делители в строке таблицы также должны следовать в порядке возрастания.

def p(x):
    return all(x % y for y in range(2, int(x ** 0.5) + 1))


def d(x):
    s = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            s |= {i, x // i}
    return sorted(s)


for x in range(125697, 125722):
    s = [i for i in d(x) if p(i)]
    if len(s) == 2 and s[0] * s[1] == x:
        print(*s)
