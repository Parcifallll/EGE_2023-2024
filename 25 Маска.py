from fnmatch import fnmatch

for i in range(65000, 700000):
    p = []
    if fnmatch(str(i), "6*97*5?"):
        for div in range(2, i+1):
            if i % div == 0 and div % 2 == 0:
                p.append(div)
    if len(p) >= 4:
        print(i, sum(p))