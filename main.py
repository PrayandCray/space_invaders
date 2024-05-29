import pygame, sys


pygame.init()
clock = pygame.time.Clock()

screen_width = 1200
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Space Invaders')
pygame.mouse.set_visible(False)
bg_color = pygame.Color('grey12')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        screen.fill(bg_color)

        pygame.display.flip()
        clock.tick(60)