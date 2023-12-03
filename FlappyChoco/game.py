import pygame
from random import randint
from choco import Chocolatine
from pipe import Pipe_bot
from pipe import Pipe_top

class Game:
    def __init__(self):
        self.running = True
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Flappy Choco")
        self.score = 0
        self.bg = pygame.image.load("Assets/background.png")
        self.choco = Chocolatine(200, 300)
        self.pipe1_bot = Pipe_bot(1000, randint(200, 450))
        self.pipe1_top = Pipe_top(1000, self.pipe1_bot.pos[1] - 675)
        self.player = pygame.sprite.Group()
        self.pipes = pygame.sprite.Group()
        self.player.add(self.choco)
        self.pipes.add(self.pipe1_bot, self.pipe1_top)
        self.font = pygame.font.Font(None, 128)
        self.t = 0

# Function to display a number on the screen
    def display_number(self, number):
        text = self.font.render(f"{number}", True, [255, 255, 255])
        self.screen.blit(text, (380, 280))

    def check_collisions(self):
            collisions = pygame.sprite.groupcollide(self.player, self.pipes, False, False)
            if collisions:
                self.running = False

    def handle_input(self):
        key_pressed = pygame.key.get_pressed()

        if key_pressed[pygame.K_SPACE] and self.choco.jump_charge >= 10:
            self.choco.jump_charge = 0
            self.choco.flapping = True

    def update(self):
        self.pipe1_bot.move()
        if self.pipe1_bot.pos[0] == 1000:
            self.score += 1
        self.pipe1_top.move(self.pipe1_bot.pos[1])
        self.choco.update()

    def run(self):

        clock = pygame.time.Clock()

        while self.running:

            self.handle_input()
            self.check_collisions()
            self.update()

            self.screen.blit(self.bg, (0, 0))
            self.display_number(self.score)
            self.screen.blit(self.pipe1_bot.sprite, (self.pipe1_bot.pos[0], self.pipe1_bot.pos[1]))
            self.screen.blit(self.pipe1_top.sprite, (self.pipe1_top.pos[0], self.pipe1_top.pos[1]))
            self.screen.blit(self.choco.sprite, (self.choco.pos[0], self.choco.pos[1]))

            pygame.display.flip()
    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            clock.tick(60)
        pygame.quit()