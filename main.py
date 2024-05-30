import pygame, sys
from player import *
from bullet import *

def callfunc():
    screen.fill(bg_color)
    player.update()
    bullet_group.draw(screen)
    player_group.draw(screen)

pygame.init()
clock = pygame.time.Clock()

screen_width = 1200
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Space Invaders')
pygame.mouse.set_visible(False)
bg_color = pygame.Color('grey12')

player = Player(screen_width / 2 - 100, screen_height - 85, 'spaceship.png', screen_width)
player_group = pygame.sprite.Group()
player_group.add(player)

bullet = Bullet(screen_width / 2 - 100, screen_height - 85, 'bullet.png')
bullet_group = pygame.sprite.Group()
bullet_group.add(bullet)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    callfunc()

    pygame.display.flip()
    clock.tick(60)