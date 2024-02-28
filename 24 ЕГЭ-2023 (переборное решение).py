f = open("Файлы/24_9753.txt")
a = f.readline().split("Y")
m = 0
for i in range(len(a) - 151):
    m = max(m, len("Y".join(a[i:i+151])))
print(m)
