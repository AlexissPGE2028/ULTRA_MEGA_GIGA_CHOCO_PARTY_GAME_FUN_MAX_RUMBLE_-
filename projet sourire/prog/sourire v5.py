import pygame
import random
import math

pygame.init()
pygame.mixer.init()
pygame.font.init()

clock = pygame.time.Clock()
pygame.display.set_caption("Sourire")


def couleur(n):
    # la fonction couleur que j'ai rajouter et la simplement pour permetre de "ranger" le code
    # on peut rajouter n'importe couleur a condition de le rajouter dans la [liste arc_en_ciel]
    # on renvoie l'information de la couleur choisi a l'aide d'un return (mieux qu'un global car economie de ram)

    white = 255, 255, 255
    gray = 206, 206, 206
    dark_gray = 95, 95, 95
    black = 0, 0, 0

    light_brown = (167, 103, 38)
    brown = (70, 46, 1)

    red = (222, 41, 22)
    green = (22, 184, 78)
    blue = (0, 127, 255)

    arc_en_ciel = [white, gray, black, light_brown, brown, red, green, blue, dark_gray]

    return arc_en_ciel[n - 1]


def texte_clique_open():
    if obj.aucun_paquet:
        x = texte_clique.taille
        if texte_clique.taille > var_x // 10:
            texte_clique.sens = -1
        if texte_clique.taille < var_x // 40:
            texte_clique.sens = 1
        if texte_clique.sens == 1:
            texte_clique.taille = x + 3
        else:
            texte_clique.taille = x - 3
        font_taille = pygame.font.Font(font.chemin, texte_clique.taille)
        texte = font_taille.render(texte_clique.texte, True, couleur(9))
        texte_rect = texte.get_rect()
        texte_rect.center = texte_clique.coo
        ecran.screen.blit(texte, texte_rect)


def effect(liste, position):
    if len(liste) == 0:
        for i in range(random.randint(50, 200)):
            liste.append(Particle(position, 5, random.randint(1, 20) * 0.1, random.randint(270, 270),
                                  random.choice([(200, 200, 200),
                                                 (150, 150, 150),
                                                 (255, 255, 50),
                                                 (130, 130, 130),
                                                 (10, 10, 10),
                                                 (180, 180, 180),
                                                 (119, 136, 153)])))

    for p in liste:
        n = p.radius
        if n > 0:
            p.move()
            p.draw()

            # partie affichage
            n -= 0.1
            p.radius = n
        else:
            liste.remove(p)


class ecran:
    infoObject = pygame.display.Info()
    size = (infoObject.current_w // 2, infoObject.current_h // 2)
    screen = pygame.display.set_mode(size, pygame.RESIZABLE)


var_x, var_y = ecran.screen.get_width(), ecran.screen.get_height()


class font:
    chemin = None
    font = pygame.font.Font(chemin, 800 // 70)


class image:
    def __init__(self, ymage=None):
        self.ymage = pygame.image.load(ymage)
        self.image_clone = self.ymage
        self.rect = None

    def resize(self, size):
        x, y = size
        largeur = x
        hauteur = largeur * self.ymage.get_height() / self.ymage.get_width()
        if hauteur > y * 0.7:  # too tall for screen
            largeur = largeur * (y * 0.7) / hauteur  # reduce width to keep ratio
            hauteur = y * 0.7
        self.image_clone = pygame.transform.scale(self.ymage, (largeur, hauteur))

    def affiche(self, coo, surface_affiche):
        self.rect = self.image_clone.get_rect()
        self.rect.center = coo
        surface_affiche.blit(self.image_clone, self.rect)


class paquet:

    def __init__(self, n_carte=None, coo=None):
        self.n_carte = n_carte
        self.liste = []
        self.coo = coo
        self.image_booster = None

    def creer_carte(self):
        for i in range(self.n_carte):
            karte = carte(i, self.coo)
            karte.rarete()
            karte.chemin_carte()
            self.liste.append(karte)

    def image_packet(self):
        chemin = "../index/chemin_image/image booster.txt"
        with open(chemin, 'r') as file:
            lire = file.read()
            ligne = lire.split("\n")
            choix = random.choice(ligne)
            self.image_booster = image(choix)
            file.close()


class carte:

    def __init__(self, index=None, coo=None):
        self.index = index
        self.rare = None
        self.image_chemin = None
        self.id = None
        self.coo = coo
        self.image = None

    def rarete(self):
        random_rare = "0" * 1000 + "1" * 500 + "2" * 250 + "3" * 120 + "4" * 60 + "5" * 30
        dico_rare = {"0": "commun",
                     "1": "un-commun",
                     "2": "rare",
                     "3": "epic",
                     "4": "legendaire",
                     "5": "Godess"}
        self.rare = dico_rare[random.choice(random_rare)]

    def chemin_carte(self):
        chemin = '../index/chemin_image/' + self.rare + '.txt'
        with open(chemin, 'r') as file:
            lire = file.read()
            ligne = lire.split("\n")
            rdom = random.choice(ligne)
            splitRDom = rdom.split("#")
            self.image_chemin = splitRDom[0]
            self.id = splitRDom[1]
            file.close()
            self.image = image(self.image_chemin)

    def mouvement(self, coov2, speed):
        x, y = self.coo
        x2, y2 = coov2
        px, py = x, y
        radians = math.atan2(y2 - py, x2 - px)
        distance = math.hypot(x2 - px, y2 - py)
        distance = int(distance)
        dx = math.cos(radians)
        dy = math.sin(radians)
        if distance > 0:
            distance -= 1
            x += dx * speed
            y += dy * speed
        else:
            return
        self.coo = x, y


class text:

    def __init__(self, texte=None, taille=None, sens=None, coo=None, color=None):
        self.texte = texte
        self.taille = taille
        self.sens = sens
        self.coo = coo
        self.color = color

    def show(self, letexte):
        font_taille = pygame.font.Font(font.chemin, self.taille)
        texte = font_taille.render(letexte, True, self.color)
        texte_rect = texte.get_rect()
        texte_rect.center = self.coo
        ecran.screen.blit(texte, texte_rect)


class Particle:
    def __init__(self, coo, radius, speed, angle, colour):
        x, y = coo
        self.x = x
        self.y = y
        self.speed = speed
        self.angle = angle
        self.radius = radius
        self.colour = colour
        self.rect = pygame.draw.circle(ecran.screen, (255, 255, 0),
                                       (int(round(x, 0)),
                                        int(round(y, 0))),
                                       self.radius)

    def move(self):
        self.x += math.sin(self.angle) * self.speed
        self.y -= math.cos(self.angle) * self.speed
        self.rect.x = int(round(self.x))
        self.rect.y = int(round(self.y))

    def draw(self):
        x = self.x
        y = self.y
        pygame.draw.circle(ecran.screen, self.colour, (int(round(x, 0)),
                                                       int(round(y, 0))), self.radius)


class son:
    chemin_whoosh = "../index/son/effect/whoosh1.mp3"
    whoosh = pygame.mixer.Sound(chemin_whoosh)
    volume = 1


class obj:
    rn = True
    aucun_paquet = True
    liste_particle_click = []


texte_clique = text("Click to OPEN", var_x // 80, -1, (var_x // 2, var_y // 2))  # le sens est -1 decroissan 1 croissant
texte_fps = text(str(clock.get_fps()), var_x // 20, None, (var_x // 40, var_y // 20), (0, 0, 0))

pak = paquet(1, (var_x//2, var_y//2))
pak.image_packet()
pak.image_booster.resize((var_x // 2, var_x // 2))
pak.creer_carte()

while obj.rn:

    ecran.screen.fill(couleur(1))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.mixer.quit()
            pygame.font.quit()
            pygame.quit()

        if event.type == pygame.VIDEORESIZE:
            pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            var_x, var_y = ecran.screen.get_width(), ecran.screen.get_height()
            font.font = pygame.font.Font(font.chemin, 800 // 70)
            texte_clique = text("Click to OPEN", var_x // 80, -1, (var_x // 2, var_y // 2))
            pak.image_booster.resize((var_x // 2, var_x // 2))

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                obj.liste_particle_click.append(([], pygame.mouse.get_pos()))

    texte_clique_open()
    for j in obj.liste_particle_click:
        if len(j[0]) == 1:
            obj.liste_particle_click.remove(j)
        else:
            effect(j[0], j[1])
    texte_fps.show(str(int(clock.get_fps())))
    pak.image_booster.affiche((var_x//2, var_y//2), ecran.screen)
    for te in pak.liste:
        te.image.resize((var_x//2, var_x//2))
        te.image.affiche(te.coo, ecran.screen)
        te.mouvement((0, 0), 10)
    pygame.display.flip()

    clock.tick(65)
