def f(x):
    return ((x % 6 == 0) <= (x % 14 != 0)) or (x + a >= 85)
for a in range(1,100):
    if all(f(x) == 1 for x in range(1,1000)):
        print(a)