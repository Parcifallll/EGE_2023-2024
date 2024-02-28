#Состоит из символов "A, B, C, D, E, F". AF-подстрока = "A" + ... + "F" (граничные символы входят в подстроку). Найти min длину AF-подстроки.
# Подстроки, состоящие из двух символов, не учитывать.
f = open("../Файлы/24-2.txt")
s = f.readline()
m = len(s)
posA = None
for i in range(len(s)):
    if s[i] == "A":
        posA = i #позиция "A"
    elif s[i] == "F":
        if posA != None: #Если нашли "А"
            m = min(m, i - posA + 1) # кол-во элементов от posA до i = (i - posA) + 1
print(m)
