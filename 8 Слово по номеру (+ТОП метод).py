from itertools import product

print(list(product("косф", repeat=5))[267 - 1]) # ОФИГЕТЕЛЬНОЕ решение от ТФ
# cnt = 0
# for x in product("косф", repeat=5):
#     cnt += 1
#     if cnt == 267:
#         print(x)
#         break
