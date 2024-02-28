# Дана цепочка из символов A, B, C, D, E, F. Найдите
# максимальную длину цепочки вида EBCFEBCFEBCF (состоящей из фрагментов EBCF, последний фрагмент может быть неполным).
f = open("../Файлы/k7b-4.txt")
s = f.readline()
state = 0  # Ждем E
n = 0
m = 0
for i in range(len(s)):
    if state == 0 and s[i] == "E":
        state = 1  # Ждем B
        n += 1
    elif state == 1 and s[i] == "B":
        state = 2  # Ждем C
        n += 1
    elif state == 2 and s[i] == "C":
        state = 3  # Ждем F
        n += 1
    elif state == 3 and s[i] == "F":
        state = 0  # Снова ждем E
        n += 1
    else:  # Снова ждем Е, причем цепочка нарушилась
        state = 0 #Ждем Е
        m = max(n, m)
        n = 0

print(m)

