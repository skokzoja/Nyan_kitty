import random

import pygame

pygame.init()
ozadje = pygame.image.load("nyan_cat_background_by_kento1_d3l6i50-pre.jpg")
canvas = pygame.display.set_mode((500,500))
ozadje = pygame.transform.scale(ozadje, (500, 500))
muc = pygame.image.load("muc.png")
muc = pygame.transform.scale(muc, (250, 250))
klobasa = pygame.image.load("klobasa.png")
klobasa = pygame.transform.scale(klobasa, (200, 50))

pygame.display.set_caption("Nyan Cat")
x = 0
y = 100
hitrost =   1
gravitacija = 0.05
exit = False

# [ [ sirina,[x, y]], ... ]
platforme = [ [50,[200,300]], [32, [229, 400]], [65, [350, 150]], [ 45, [400, 50]],  [ 30, [500, 200]]]

def novaPlatforma():
    Nsirina = random.randint(30,90)
    Nx = 500
    Ny = random.randint(150,400)
    platforme.append([Nsirina,[Nx,Ny]])

while not exit:
    pygame.time.wait(10)
    canvas.blit(ozadje, (0, 0))

    hitrost += gravitacija
    y += hitrost

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        hitrost = -4

    print(platforme)

    kitty = pygame.Rect(x,y,15, 15)
    canvas.blit(muc, kitty)

    for i in platforme:
        i[1][0] -= 1.5
        plat =  pygame.Rect(i[1][0],i[1][1], i[0],10 )
        canvas.blit(klobasa, plat)
        if i[1][0] < -i[0]:
            novaPlatforma()
            platforme.pop(0)
        if kitty.colliderect(plat):
            print(":)")



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

    pygame.display.update()