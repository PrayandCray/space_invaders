import pygame
from player import *

pygame.init()

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, picture_path):
        self.image = pygame.image.load(picture_path)
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y