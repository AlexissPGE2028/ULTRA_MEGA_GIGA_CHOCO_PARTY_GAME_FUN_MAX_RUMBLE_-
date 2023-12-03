import pygame

class Chocolatine(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.sprite = pygame.image.load("Assets/choco.png")
        self.sprite.set_colorkey([0, 0, 0])
        self.sprite = pygame.transform.scale(self.sprite, (100, 100))
        self.rect = self.sprite.get_rect()
        self.rect.topleft = (x, y)
        self.pos = [x, y]
        self.flapping = False
        self.power = 15
        self.gravity = 2
        self.jump_charge = 0

    def flap(self):
        if self.flapping == True and self.jump_charge < 10:
            self.pos[1] -= self.power
            self.gravity = 1
        if self.jump_charge >= 7:
            self.flapping = False


    def collide_window(self):
        if self.pos[1] > 520:
            self.pos[1] = 520
        if self.pos[1] < -20:
            self.pos[1] = -20

    def update(self):
        self.jump_charge += 1
        self.pos[1] += self.gravity
        self.gravity *= 1.035
        self.flap()
        self.collide_window()
        self.rect.topleft = (self.pos[0], self.pos[1])