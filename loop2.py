from turtle import *

pencolor('red')
bgcolor('black')
speed('fastest')
n = 0
while n <=200:
    fd(100 + n)
    rt(360/7)
    write(n,font=('normal', 15))
    n +=5

hideturtle()
mainloop()