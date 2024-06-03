from turtle import *
tracer(0)
r = 25
lt(255)
for i in range(3):
    lt(30)
    for j in range(4):
        fd(10*r)
        lt(90)
up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x*r, y*r)
        dot(3, "red")
mainloop()
update()