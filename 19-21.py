from functools import lru_cache


def moves(x):
    return x + 1, x * 2


@lru_cache
def res(x):
    if any(m >= 169 for m in moves(x)): return "win1"
    if all(res(m) == "win1" for m in moves(x)): return "loss1"
    if any(res(m) == "loss1" for m in moves(x)): return "win2"
    if all(res(m) == "win2" for m in moves(x)): return "loss2"
    if all(res(m) == "win1" or res(m) == "win2" for m in moves(x)): return "loss12"
# for x in range(1, 169):
#     if res(x) == "loss12":
#         print(x)
print(res(81))