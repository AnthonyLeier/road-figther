import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, image, posX, posY, speed):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.posX = posX
        self.posY = posY
        self.speed = speed
        self.rect.center = [self.posX, self.posY]

    def update(self, direction):
        if direction == "right":
            self.posX += self.speed
        else:
            self.posX -= self.speed  
        self.rect.center = [self.posX, self.posY]