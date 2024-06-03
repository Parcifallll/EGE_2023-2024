s = open("../Файлы/24_4643.txt").readline().replace("B", "A").replace("2", "1")
m = [0]*len(s) #Динамическое программирование
for i in range(2, len(s)):
    if s[i-2:i+1] == "11A":
        m[i] = m[i-3] + 1
print(max(m))
# for i in range(400): #Узнаем ол-во таких цепочек в строке через поиск
#     if i*"11A" in s:
#         print(i)
#     else:
#         break

# s = s.replace("11A", "*").replace("A", " ").replace("1", " ") #Заменой
# print(max(len(i) for i in s.split()))