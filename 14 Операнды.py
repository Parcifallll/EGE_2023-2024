num = list(range(10)) + list("ABCDE")
for x in num:
    y = int(f"123{x}5", 15) + int(f"1{x}233", 15)
    if y % 14 == 0:
        print(x, y // 14)

