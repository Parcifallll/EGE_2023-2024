from itertools import permutations
# Кол-во всех 16ричных трехзначных чисел, в которых все цифры различны и никакие две четные или две нечетные не стоят рядом
cnt = 0
for x in permutations("0123456789ABCDEF", r=3):
    x = "".join(x)
    if (x[0] != "0" and all(z + z not in x for z in "02468ACE" )
            and all(z + y not in x for z in "13579BDF" for y in "13579BDF")):
        #Чтобы вручную не делить на множество из символов, приводим строку к списку строк
        cnt += 1
print(cnt)
