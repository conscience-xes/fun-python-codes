from turtle import *
import random as r
import colorsys as col

bgcolor('black')
screen = Screen()
screen.tracer(0,0)
n = 50
army = [
    Turtle() for i in range(n)
]
k = 0
for T in army:
    c = col.hsv_to_rgb(k,1,1)
    k += 1/n
    T.color(c)
    T.up()
    T.goto(
        r.uniform(-500,500),
        r.uniform(-500,500)
    )

def next():
    for i in range(n):
        angl = army[i].towards(
            army[(i+1) %n]
        )
        army[i].seth(angl)
    for T in army:
        T.forward(3)
    screen.update()
    screen.ontimer(next, i)
next()
done()