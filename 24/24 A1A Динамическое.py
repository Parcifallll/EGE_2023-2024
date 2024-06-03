#Содержит ABC123. Найти кол-во ТРОЕК буква + цифра + буква.
s = open("../Файлы/24-157.txt").readline()
for i in "ABC123":
    if i in "ABC":
        s = s.replace(i, "A")
    else: s = s.replace(i, "1")
m = [0]*len(s)
for i in range(2, len(s)):
    if s[i-2] + s[i-1] + s[i] == "A1A":
        m[i] = m[i-3] + 1 #Из-за того, что проверяем ТРОЙКИ
print(max(m))