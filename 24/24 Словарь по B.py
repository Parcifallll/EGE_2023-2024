#В каждой строке определяется самая частая буква перед которой стоит "В". Если таких букев несколько - в список заносятся ВСЕ (из-за это ответ меняется).
# Найти самую частую букву из полученного списка
f = open("../Файлы/24_DsZaFzI.txt")
m = []
for i in f:
    d = {}
    for j in range(1, len(i)):
        if i[j-1] == "B":
            if i[j] not in d:
                d[i[j]] = 1
            else: d[i[j]] += 1
    while len({i: d[i] for i in d if d[i] == d[max(d, key=d.get)]}) > 1:
        m.append(max(d, key=d.get))
        del d[max(d, key=d.get)]
    m.append(max(d, key=d.get))
print(max(m.count(i) for i in m))
