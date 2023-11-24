a = [None] * 100
for i in range(1, 89):
    if i <= 5:
        a[i] = 2 + i
    elif i > 5 and i % 2 == 0:
        a[i] = a[i - 2] + 2 * a[i // 2] - i
    else:
        a[i] = a[i - 1] + a[i - 2] + i
print(a[97] - a[88])
