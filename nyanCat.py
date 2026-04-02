import random

import pygame

pygame.init()
pygame.mixer.init()
ozadje = pygame.image.load("nyan_cat_background_by_kento1_d3l6i50-pre.jpg")
canvas = pygame.display.set_mode((800, 800))
ozadje = pygame.transform.scale(ozadje, (800, 800))
muc = pygame.image.load("muc.png")
muc = pygame.transform.scale(muc, (250, 250))


pygame.display.set_caption("Nyan Cat")
pygame.mixer.music.load("Nyan Cat original (1).mp3")
pygame.mixer.music.play(-1)

x = 150
y = 100
hitrost =   5
gravitacija = 0.07
exit = False

# [ [ sirina,[x, y]], ... ]
platforme = [ [160,[200,340]], [200, [229, 400]], [140, [350, 580]], [ 180, [400, 60]],  [ 220, [500, 640]]]
visine = [160, 220, 280, 340, 400, 460, 520, 580, 640, 700]

def novaPlatforma():
    Nsirina = random.randint(140,300)
    Nx = 800
    Ny = random.choice(visine)
    platforme.append([Nsirina,[Nx,Ny]])

while not exit:
    pygame.time.wait(50)
    canvas.blit(ozadje, (0, 0))
    naPlatformi = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        hitrost = -5

    print(platforme)
    print(x,y)

    kitty = pygame.Rect(x,y,65, 65)
    pygame.draw.rect(canvas, (150, 0, 250), kitty)

    for i in platforme:
        i[1][0] -= 1.5
        plat =  pygame.Rect(i[1][0],i[1][1], i[0],20 )
        pygame.draw.rect(canvas, (222, 91, 40), plat)
        if i[1][0] < -i[0]:
            novaPlatforma()
            platforme.pop(0)

        if kitty.colliderect(plat):
            print(":)")
            if hitrost >= 0 and kitty.bottom <= plat.bottom:
                y = plat.top - kitty.height
                hitrost = 0
                naPlatformi = True

    if naPlatformi == False:
        print("------------------------")
        hitrost += gravitacija
        y += hitrost



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

    pygame.display.update()