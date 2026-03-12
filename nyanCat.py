import pygame

pygame.init()

canvas = pygame.display.set_mode((500,500))

pygame.display.set_caption("Moje okno")
rdec = pygame.Rect(80,30,15,15)

exit = False

while not exit:
    pygame.time.wait(4)
    canvas.fill((0, 0, 0))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

    pygame.draw.rect(canvas,barvaR, rdec)
#-------

    pygame.display.update()