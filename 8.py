from itertools import permutations

# ФОКСИК чтобы никакие две гласные не стояли рядом
cnt = 0
for i in set(permutations("фоксик", r=6)):  # обязательно берем set тк две буквы К
    x = "".join(i)
    if all(f not in x for f in {"ои", "ии", "оо", "ио"}):
        cnt += 1
print(cnt)
