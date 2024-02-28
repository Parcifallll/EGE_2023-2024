import itertools
cnt = 0
for x in set(itertools.permutations("выигрывать", r=10)): #Если есть повторы букв - ВСЕГДА берем set
    b = "".join(x)
    if x[0] != "ь" and all(x + y not in b for x in "ыиа" for y in "ыиа"): #Никакие две гласные не стоят рядом
        cnt += 1
print(cnt)

