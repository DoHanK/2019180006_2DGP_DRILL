import turtle
from turtle import *

for j in range(1,7):
     forward(500)
     penup()
     goto(0,100*j)
     pendown()
right(90)
for i in range(0,6):
    penup()
    goto(100*i,500)
    pendown()
    forward(500)
  
