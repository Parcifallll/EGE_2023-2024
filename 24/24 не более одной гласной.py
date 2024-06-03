#Символы идут в алфавитном порядке + в последовательности находится не более одной гласной (AEIOUY).
a = open("../Файлы/24 (2).txt").readline()
m = l = r = k = 0
for r in range(len(a)):
    if a[r] in "AEIOUY": k += 1
    if a[r] >= a[r - 1]:
        while k > 0:
            if a[l] in "AEIOUY": k -= 1
            l += 1
        m = max(m, r - l + 1)
    else:
        l = r
        k = a[r] in "AEIOUY"
print(m)
