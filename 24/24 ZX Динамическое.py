#Проверяем ПАРЫ - поэтому в 6 строке смотрим на m[i-2] символ
s = open("../Файлы/24-157.txt").readline()
m = [0]*len(s)
for i in range(2, len(s)):
    if s[i-1] + s[i] == "ZX" or s[i-1] + s[i] == "ZY":
        m[i] = m[i-2] + 1
print(max(m))