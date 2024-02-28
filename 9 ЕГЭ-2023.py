# Записаны 4 числа. В строке есть только 1 число, которое повторяется дважды. Остальные различны.
# Повторяющееся число не меньше среднего арифм четырех неповторяющихся
f = open("Файлы/99.txt")
k = 0
for i in f:
    k += 1
    a = [int(i) for i in i.split()]
    rep = [i for i in a if a.count(i) == 2]
    nonrep = [i for i in a if a.count(i) == 1]
    if len(rep) == 2 and len(nonrep) == 2 and (rep[0] >= sum(nonrep)/2): #Условие про nonrep писать НУЖНО!
        print(k)
        break
