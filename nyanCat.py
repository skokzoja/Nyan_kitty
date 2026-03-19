import random

import pygame

pygame.init()

canvas = pygame.display.set_mode((500,500))

pygame.display.set_caption("Moje okno")
x = 150
y = 100
hitrost =   1
gravitacija = 0.05
exit = False

# [ [ sirina,[x, y]], ... ]
platforme = [ [50,[200,300]], [32, [229, 400]], [65, [350, 150]], [ 30, [500, 200]]]

def novaPlatforma():
    Nsirina = random.randint(30,90)
    Nx = 500
    Ny = random.randint(150,400)
    platforme.append([Nsirina,[Nx,Ny]])

while not exit:
    pygame.time.wait(10)
    canvas.fill((0, 0, 0))
    hitrost += gravitacija
    y += hitrost

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        hitrost = -4


    #novaPlatforma()
    print(platforme)

    for i in platforme:
        i[1][0] -= 1.5
        plat =  pygame.Rect(i[1][0],i[1][1], i[0],5 )
        pygame.draw.rect(canvas, (150, 0, 250), plat)

    kitty = pygame.Rect(x,y,15, 15)
    pygame.draw.rect(canvas, (150,0,250), kitty)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

    pygame.display.update()