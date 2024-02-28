from itertools import product

print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (w <= (not z)) and y and (x <= w):
                    print(x, y, z, w)

# for x, y, z, w in product([0, 1], repeat=4):
#     if (w <= (not (z))) and y and (x <= w):
#         print(x, y, z, w)
#Пишется БЫСТРЕЕ первого способа (затем аналитика)
