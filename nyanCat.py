import random
import pygame

pygame.init()
pygame.mixer.init()
ozadje = pygame.image.load("nyan_cat_background_by_kento1_d3l6i50-pre.jpg")
canvas = pygame.display.set_mode((800, 800))
ozadje = pygame.transform.scale(ozadje, (800, 800))
muc = pygame.image.load("muc.png")
muc = pygame.transform.scale(muc, (250, 70))
mafin = pygame.image.load("mafin.png")
mafin = pygame.transform.scale(mafin, (60, 60))
burger = pygame.image.load("burger.png")
burger = pygame.transform.scale(burger, (60, 60))
donut = pygame.image.load("donut.png")
donut = pygame.transform.scale(donut, (60, 60))
menu = [mafin, burger, donut]

pygame.display.set_caption("Nyan Cat")
pygame.mixer.music.load("Nyan Cat original (1).mp3")
pygame.mixer.music.play(-1)

x = 200
y = 100
hitrost =   5
gravitacija = 0.07
skoki = 2
score = 0
exit = False

# [ [ sirina,[x, y]], ... ]
platforme = [ [160,[200,340]], [200, [229, 400]], [140, [350, 580]], [ 180, [400, 60]],  [ 220, [500, 640]]]
#[ [x,y], ...]
hrana = []
#platforme = [ [160,[200,340]], , [140, [350, 580]], ,  [ 220, [500, 640]]]
visine = [160, 220, 280, 340, 400, 460, 520, 580, 640, 700]

for k in range(10):
    hrana.append([random.randint(0, 800), random.randint(50, 750), random.choice(menu)])
print(hrana)
def novaPlatforma():
    Nsirina = random.randint(140,300)
    Nx = 800
    Ny = random.choice(visine)
    platforme.append([Nsirina, [Nx, Ny]])
platforme = [ [50,[200,340]], [200, [250, 400]], [140, [380, 580]], [ 180, [430, 460]], [ 100, [510, 160]],  [ 110, [660, 220]], [ 150, [780, 400]]]

def novaHrana():
    Hx = 800
    Hy = random.randint(150, 700)
    hrana.append([Hx, Hy, random.choice(menu)])

while not exit:
    pygame.time.wait(5)
    canvas.blit(ozadje, (0, 0))
    naPlatformi = False

    if y > 800:
        exit = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and skoki > 0:
                hitrost = -5
                skoki -= 1

    kitty = pygame.Rect(x,y,50, 50)
    pygame.draw.rect(canvas, (150, 0, 250), kitty)
    muc_rect = muc.get_rect()
    muc_rect.midright = kitty.midright
    canvas.blit(muc, muc_rect)

    for i in platforme:
        i[1][0] -= 1.5
        plat =  pygame.Rect(i[1][0],i[1][1], i[0],20 )
        pygame.draw.rect(canvas, (222, 91, 40), plat)
        if i[1][0] < -i[0]:
            novaPlatforma()
            platforme.pop(0)

        if kitty.colliderect(plat):
            if hitrost >= 0 and kitty.bottom <= plat.bottom:
                y = plat.top - kitty.height
                hitrost = 0
                if naPlatformi == False:
                    skoki = 2
                naPlatformi = True

    if naPlatformi == False:
        hitrost += gravitacija
        y += hitrost

    for h in hrana:
        h[0] -= 1.5
        food = pygame.Rect(h[0], h[1], 1, 1)
        pygame.draw.rect(canvas, (0, 0, 0), food)
        canvas.blit(h[2], food.topleft)
        if h[0] < 0:
            novaHrana()
            hrana.remove(h)
        if kitty.colliderect(food):
            hrana.remove(h)
            novaHrana()
            score += 1
            pygame.display.set_caption("Score:" + str(score))


    pygame.display.update()
print("Score:" + str(score))