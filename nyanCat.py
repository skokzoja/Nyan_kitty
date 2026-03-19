import pygame

pygame.init()

canvas = pygame.display.set_mode((500,500))

pygame.display.set_caption("Moje okno")
x = 200
y = 300
hitrost =   1
gravitacija = 0.1
exit = False

while not exit:
    pygame.time.wait(10)
    canvas.fill((0, 0, 0))
    hitrost += gravitacija
    y += hitrost

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        hitrost = -4


    kitty = pygame.Rect(x,y,15, 15)
    pygame.draw.rect(canvas, (150,0,250), kitty)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

    pygame.display.update()