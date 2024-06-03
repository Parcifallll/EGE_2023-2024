s = open("../Файлы/24-157.txt").readline().strip()  # Из-за того что в конце файла есть переход на новую строку берем STRIP. Не забываем!!!
d = {x: s.count(x) for x in sorted(set(s))} #Отсортированный словарь
print({i: d[i] for i in d if d[i] == d[max(d, key=d.get)]}) #Список самых частых элементов
