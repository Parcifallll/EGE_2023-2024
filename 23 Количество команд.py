#Сколько программ из 7 команд?
def f(a, b, k): #Третий параметр - кол-во команд
    if a == b: return k == 7  # Если мы пришли в нужное число, но кол-во команд != 7, возвращаем либо 0 либо 1
    if a > b: return 0
    if a < b: return f(a + 1, b, k + 1) + f(a + 4, b, k + 1) + f(a * 2, b, k + 1)


print(f(3, 27, 0))
