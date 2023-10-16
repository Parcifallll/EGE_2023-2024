s = "6"*110 + 23*"5"
while any(i in s for i in ["6666", "5555"]):
    s = s.replace("6666", "55", 1)
    s = s.replace("5555", "66", 1)
print(s)
#Если ТОЛЬКО IF без ELSE ТО УСЛОВИЯ НЕ ПИШЕМ!!! 