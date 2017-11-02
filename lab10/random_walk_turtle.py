import turtle
import random

trey = turtle.Turtle()
trey.speed(10)
stop_rule=500
while (-stop_rule < trey.xcor() < stop_rule) and (-stop_rule < trey.ycor() < stop_rule):
  trey.forward(10)
  a = random.randrange(0,360,2)
  trey.right(a)
