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
font = pygame.font.SysFont("Arial", 30)

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
    #hrana.append([random.randint(0, 800), random.randint(50, 750)])
    hrana.append([random.randint(0, 800), random.randint(50, 750), random.choice(menu)])
#print(hrana)

def novaPlatforma():
    Nsirina = random.randint(140,300)
    Nx = 800
    Ny = random.choice(visine)
    if random.random() < 0.1:
        oblika = "razpada"
    else:
        oblika = "navadna"
    platforme.append([Nsirina, [Nx, Ny],oblika])
platforme = [ [50,[200,340],"navadna"], [200, [250, 400],"navadna"], [140, [380, 580],"navadna"], [ 180, [430, 460],"razpada"], [ 100, [510, 160],"navadna"],  [ 110, [660, 220],"navadna"], [ 150, [780, 400],"navadna"]]
"""
def novaPlatforma():
    Nsirina = random.randint(50,140)
    Nx = 800
    Ny = random.randint(150,700)"""


def novaHrana():
    Hx = 800
    Hy = random.randint(150, 700)
    hrana.append([Hx, Hy, random.choice(menu)])

while not exit:
    pygame.time.wait(5)
    text = font.render(("Score:" + str(score)),True,(255,255,255))
    canvas.blit(ozadje, (0, 0))
    canvas.blit(text, (700, 10))
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


    for i in platforme:
        i[1][0] -= 1.5
        plat =  pygame.Rect(i[1][0],i[1][1], i[0],20 )
        if i[2] == "navadna":
            pygame.draw.rect(canvas, (222, 91, 40), plat)
        else:
            pygame.draw.rect(canvas, (0, 250, 40), plat)
        if i[1][0] < -i[0]:
            novaPlatforma()
            platforme.pop(0)

        if kitty.colliderect(plat):
            if hitrost >= 0 and kitty.bottom <= plat.bottom:
                if i[2] == "navadna":
                    y = plat.top - kitty.height
                    hitrost = 0

                    if naPlatformi == False:
                        skoki = 2
                    naPlatformi = True
                    cas = 10
                else:
                    skoki = 2
                    if cas != 0:
                        hitrost = 0
                        cas -= 1
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
            #pygame.display.set_caption("Score:" + str(score))


    pygame.draw.rect(canvas, (30, 55, 140), kitty)
    muc_rect = muc.get_rect()
    muc_rect.bottomright = kitty.bottomright
    canvas.blit(muc, muc_rect)


    pygame.display.update()
print("Score:" + str(score))

