# 123x23 + 635x78 (27 CC) - Продвинутая схема Горнера
for x in range(27):
    s = int("123023", 27) + x * 27 ** 2
    d = int("635078", 27) + x * 27 ** 2
    if (s + d) % 26 == 0:
        print((s + d) // 26)
