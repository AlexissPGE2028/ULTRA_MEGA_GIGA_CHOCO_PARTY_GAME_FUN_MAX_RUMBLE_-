import pygame
from random import randint
from choco import Chocolatine
from pipe import Pipe_bot
from pipe import Pipe_top

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Flappy Choco")
        self.bg = pygame.image.load("Assets/background.png")
        self.choco = Chocolatine(200, 300)
        self.pipe1_bot = Pipe_bot(1000, randint(150, 400))
        self.pipe1_top = Pipe_top(1000, self.pipe1_bot.pos[1] - 600)
        self.t = 0

    def handle_input(self):
        key_pressed = pygame.key.get_pressed()

        if key_pressed[pygame.K_SPACE] and self.choco.jump_charge >= 10:
            self.choco.jump_charge = 0
            self.choco.flapping = True

    def update(self):
        self.pipe1_bot.move()
        self.pipe1_top.move(self.pipe1_bot.pos[1])
        self.choco.update()

    def run(self):

        clock = pygame.time.Clock()

        running = True

        while running:

            self.handle_input()
            self.update()

            self.screen.blit(self.bg, (0, 0))
            self.screen.blit(self.pipe1_bot.sprite, (self.pipe1_bot.pos[0], self.pipe1_bot.pos[1]))
            self.screen.blit(self.pipe1_top.sprite, (self.pipe1_top.pos[0], self.pipe1_top.pos[1]))
            self.screen.blit(self.choco.sprite, (self.choco.pos[0], self.choco.pos[1]))

            pygame.display.flip()
    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            clock.tick(60)
        pygame.quit()