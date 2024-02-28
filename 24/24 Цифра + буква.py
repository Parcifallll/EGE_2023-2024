f = open("../Файлы/24-264.txt")
a = f.readline()
nums = "0123456789"
n = 1
m = 0
for i in range(len(a) - 1):
    if (a[i] in nums) != (a[i + 1] in nums):
        n += 1
    else:
        m = max(m, n)
        n = 1
print(m)
