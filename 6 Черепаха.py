from turtle import *
screensize(10000,10000) #Можно полистать вверх-вниз и вправо-влево
tracer(0) #Отрисовываем в один кадр
r = 25 #Увеличиваем размер клетки
for i in range(7):
    rt(90)
    fd(4*r)
    for j in range(2):
        lt(90)
        fd(4*r)
up() #Поднимаем перо
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x*r, y*r) #Переходим на координату
        dot(3, "red") #Ставится красная точка размером 3 пикселя

update() #Обновляем
mainloop() #Чтобы не пропадало