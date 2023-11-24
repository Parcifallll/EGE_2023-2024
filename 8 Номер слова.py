import itertools

cnt = 0
for i in itertools.product("аклош", repeat=5):
    cnt += 1 # cnt увеличиваем СРАЗУ ЖЕ тк отсчет слов начинается именно с ЕДИНИЦЫ а ищем порядковый номер
    if "".join(i) == "школа": #склеиваем i в слово
        print(cnt)
