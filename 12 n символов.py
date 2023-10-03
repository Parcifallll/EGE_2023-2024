def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return 0
    return 1


for n in range(1, 100):
    s = ">" + "0" * 39 + "1" * n + "2" * 39
    while ">1" in s or ">2" in s or ">0" in s:
        if ">1" in s:
            s = s.replace(">1", "22>", 1)
        if ">2" in s:
            s = s.replace(">2", "2>", 1)
        if ">0" in s:
            s = s.replace(">0", "1>", 1)
    if isPrime(sum(int(i) for i in s if i != ">")):
        print(n)
        break
