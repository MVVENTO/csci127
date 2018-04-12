import turtle
import random

trey = turtle.Turtle()
trey.speed(10)

for i in range(1000):
  trey.forward(10)
  a = random.randrange(0,360,1)
  trey.right(a)
