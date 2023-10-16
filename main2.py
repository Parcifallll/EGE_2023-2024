f = open("17-1.txt")
a = [int(i) for i in f]
p = []
for i in range(len(a) - 1):
    x, y = a[i], a[i + 1]
    if ((abs(x) % 9 == 0 and oct(abs(y))[2:][-1] == "3" and abs(y) % 9 != 0)
            or (abs(y) % 9 == 0 and oct(abs(x))[2:][-1] == "3" and abs(x) % 9 != 0)):
        p.append(max(x, y))
print(len(p), max(p))
