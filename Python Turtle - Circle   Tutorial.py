from turtle import *
bgcolor("black")
pensize(4)
speed(0)
for i in range(20):
    for colours in  ["red", "magenta", "blue","cyan","green","yellow","white", "#CC00CC"]:
        color(colours)
        circle(150)
        left(4)
hideturtle()
