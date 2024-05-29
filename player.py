import pygame, sys

pygame.init()

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, picture):
        super().__init__()
        self.image = pygame.image.load(picture)
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()