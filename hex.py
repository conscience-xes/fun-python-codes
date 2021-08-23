from turtle import *
hideturtle()

colors = ['cyan', 'green', 'blue']

bgcolor('black')

b = 1
while True:
    color(colors[b % 3])
    forward(b)
    left(59)
    b = b + 1
done()