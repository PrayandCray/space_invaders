import pygame, sys

pygame.init()

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, picture):
        super().__init__()
        self.image = pygame.image.load(picture)
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.speed = 10

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed

    def update(self):
        self.get_input()