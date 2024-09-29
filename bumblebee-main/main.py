import pgzrun
import random 

WIDTH = 600
HEIGHT= 600

bee=Actor("bee")
bee.pos=100,100

flower=Actor("flower")

def draw():
    screen.blit("bg", (0,0))
    bee.draw()
    flower.draw()



pgzrun.go()
