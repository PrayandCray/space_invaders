import pygame, sys
from player import *

def callfunc():
    screen.fill(bg_color)
    player_group.draw(screen)

pygame.init()
clock = pygame.time.Clock()

screen_width = 1200
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Space Invaders')
pygame.mouse.set_visible(False)
bg_color = pygame.Color('grey12')

player = Player(screen_width / 2 - 100, screen_height - 160, 'spaceship.png')
player_group = pygame.sprite.Group()
player_group.add(player)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player.x -= 100
            if event.key == pygame.K_d:
                player.x += 100

    callfunc()

    pygame.display.flip()
    clock.tick(60)