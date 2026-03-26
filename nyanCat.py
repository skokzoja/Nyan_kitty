import random

import pygame

pygame.init()
ozadje = pygame.image.load("nyan_cat_background_by_kento1_d3l6i50-pre.jpg")
canvas = pygame.display.set_mode((800, 800))
ozadje = pygame.transform.scale(ozadje, (800, 800))
muc = pygame.image.load("muc.png")
muc = pygame.transform.scale(muc, (250, 250))
#muc = pygame.transform.scale(muc, (250, 250))
#muc = pygame.transform.scale(muc, (250, 250))
klobasa = pygame.image.load("klobasa.png")
klobasa = pygame.transform.scale(klobasa, (200, 50))


pygame.display.set_caption("Nyan Cat")
x = 150
y = 100
hitrost =   5
gravitacija = 0.07
skoki = 2
exit = False

# [ [ sirina,[x, y]], ... ]
platforme = [ [160,[200,340]], [200, [229, 400]], [140, [350, 580]], [ 180, [400, 60]],  [ 220, [500, 640]]]
visine = [160, 220, 280, 340, 400, 460, 520, 580, 640, 700]

def novaPlatforma():
    Nsirina = random.randint(140,300)
    Nx = 800
    Ny = random.choice(visine)
platforme = [ [50,[200,300]], [90, [229, 400]], [140, [350, 150]], [ 100, [400, 50]],  [ 50, [500, 200]]]

def novaPlatforma():
    Nsirina = random.randint(50,140)
    Nx = 500
    Ny = random.randint(150,400)
    platforme.append([Nsirina,[Nx,Ny]])

while not exit:
    pygame.time.wait(20)
    canvas.blit(ozadje, (0, 0))
    naPlatformi = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and skoki > 0:
        hitrost = -5
        skoki -= 1

    print(platforme)
    print(x,y)

    kitty = pygame.Rect(x,y,15, 15)
    pygame.draw.rect(canvas, (150, 0, 250), kitty)
    canvas.blit(muc, kitty)

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
                skoki = 2
                naPlatformi = True

    if naPlatformi == False:
        print("------------------------")
        hitrost += gravitacija
        y += hitrost


    if y > 500:
        exit = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

    pygame.display.update()