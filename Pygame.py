import pygame
pygame.init()
red = (255, 0, 0)
pygame.display.set_caption("The Ultimate Game")
icon = pygame.image.load('download.png')
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((1024, 720))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((red))
    pygame.display.update()
