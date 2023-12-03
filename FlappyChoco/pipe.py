from random import randint
import pygame

class Pipe_bot(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.sprite = pygame.image.load("Assets/pipe_bot.png")
        self.sprite.set_colorkey([0, 0, 0])
        self.sprite = pygame.transform.scale(self.sprite, (150, 450))
        self.rect = self.sprite.get_rect()
        self.pos = [x, y]
        self.speed = 1

    def move(self):
        self.pos[0] -= self.speed
        if self.pos[0] < -150:
            self.pos[0] = 1000
            self.pos[1] = randint(150, 400)
            self.speed += 1

class Pipe_top(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.sprite = pygame.image.load("Assets/pipe_top.png")
        self.sprite.set_colorkey([0, 0, 0])
        self.sprite = pygame.transform.scale(self.sprite, (150, 450))
        self.rect = self.sprite.get_rect()
        self.pos = [x, y]
        self.speed = 1

    def move(self, y_bot):
        self.pos[0] -= self.speed
        if self.pos[0] < -150:
            self.pos[0] = 1000
            self.pos[1] = y_bot - 600
            self.speed += 1