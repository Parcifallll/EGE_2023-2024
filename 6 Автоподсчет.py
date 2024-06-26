import turtle
from turtle import *

tracer(0) #Отрисовываем в один кадр
screensize(1000, 1000) #Масштаб вверх и вправо
color("black", "red") #Цвет границы и заливки
m = 100 #Берем большой масштаб
begin_fill() #Начинаем закрашивать фигуру
# lt(90) #Поворачиваем черепаху вдоль оси ОРДИНАТ (читаем условие)
rt(30)
for i in range(4): #Повторение цикла - РОВНО то число, которым ПОЛНОСТЬЮ закроется фигура (станет замкнутой) - подбираем сами
    fd(25 * m)
    rt(90)
end_fill() #Закрасили фигуру
canvas = getcanvas() #Получаем поле
cnt = 0
for x in range(-100 * m, 100 * m, m): #Следим, чтобы все точки убрались
    for y in range(-100 * m, 100 * m, m):
        item = canvas.find_overlapping(x, y, x, y) #Список пересечения прямоугольнкиа с исходной фигурой
        if item != (): #Ищем перемечения с черным цветом
            cnt += 1
print(cnt)
mainloop()
#Код работает ТОЛЬКО для подсчета без учета границ