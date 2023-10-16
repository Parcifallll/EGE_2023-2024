def great_common_divisor(num1, num2):
    while num2 != 0 :
        num1, num2 = num2, num1 % num2
    return num1
# Эффективный алгоритм Евклида для поиска НОД двух чисел(есть вариант через вычитаение)