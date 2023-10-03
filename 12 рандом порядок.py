limit = 30  # берем постепенно т.к. не высчитывает
for x in range(limit):
    for y in range(limit):
        for z in range(limit):
            s = "0" + "1" * x + "2" * y + "3" * z + "0"
            while "00" not in s:  # в начале и конце строки "0" поэтому идем пока не будет "00"
                s = s.replace("01", "210", 1)  # условий нет тк порядок РАНДОМНЫЙ
                s = s.replace("02", "3101", 1)
                s = s.replace("03", "2012", 1)
            if (s.count("1") == 111 and
                    s.count("2") == 101 and
                    s.count("3") == 35):
                print(x + y + z + 2) # не забываем прибавить ДВА НУЛЯ(2)
#
# limit = 30
# for x in range(limit):
#     for y in range(limit):
#         for z in range(limit):
#             s = "0" + x * "1" + y * "2" + z * "3"
#             while ("01" in s) or ("02" in s) or ("03" in s):
#                 s = s.replace("01", "210", 1)
#                 s = s.replace("02", "3101", 1)
#                 s = s.replace("03", "2302", 1)
#             if s.count("1") == 52 and s.count("2") == 33 and s.count("3") == 23:
#                 print(y) кол-во двоек в исходной строке
