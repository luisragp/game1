import pgzrun
from random import randint


WIDTH = 600
HEIGHT = 600

pineapple = Actor("pineapple")

#Pineaple on the screen
def draw():
    screen.clear()
    pineapple.draw()

#Place the pineapple on your own coordinates
def place_pineapple():
    pineapple.x = randint(10,600)
    pineapple.y = randint(10,400)

#React with mouse clics
def on_mouse_down(pos):
    #Check if the cursos is in the Same position as the apple
    if pineapple.collidepoint(pos):
        print("Good Shot!")
        place_pineapple()
    else:
        print("You Missed!")
        quit()

place_pineapple()

pgzrun.go()