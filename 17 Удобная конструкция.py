cnt = 0
for x in range(1045, 8964):
    if (x % 5 == 0 or x % 7 == 0) and all(x % i != 0 for i in (11, 13, 17, 19)):
        cnt += 1
print(cnt)
