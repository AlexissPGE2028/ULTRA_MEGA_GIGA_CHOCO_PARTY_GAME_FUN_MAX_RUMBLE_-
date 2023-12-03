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
    print(position)
    print(var_x//2, var_y//2)

    if len(liste) == 0:
        for i in range(random.randint(1, 50)):
            liste.append(particle(random.randint(1, 10), (random.randint(0, var_x), random.randint(0, var_y)),
                                  (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 255, None,
                                  random.randint(1, 20)))

    for particule in liste:
        n = particule.transp
        if n <= 0:
            liste.remove(particule)
        else:
            if particule.deplace is None:
                x, y = position
                #  partie calcule droite et pos
                x1, y1 = particule.coo
                vitesse = particule.vitesse

                angle = math.atan2((y1 - y), (x1 - x))

                if (y1 - x) < 0:
                    x += int(vitesse * math.cos(angle))
                    y += int(vitesse * math.sin(angle))

                particule.deplace = x, y
                print(particule.deplace)
            else:
                x, y = particule.deplace
                x1, y1 = particule.coo
                vitesse = particule.vitesse

                angle = math.atan2((y1 - y), (x1 - x))

                if (y1 - x) < 0:
                    x += int(vitesse * math.cos(angle))
                    y += int(vitesse * math.sin(angle))

                particule.deplace = x, y

            # partie affichage
            surface = pygame.Surface((100, 100))
            surface.set_colorkey((0, 0, 0))
            surface.set_alpha(particule.transp)
            pygame.draw.circle(surface, particule.color, (50, 50), var_x // 500 * particule.taille)
            if particule.deplace is not None:
                ecran.screen.blit(surface, particule.deplace)
            n -= 10
            particule.transp = n


def resize(n, size):

    x, y = size

    largeur = x
    hauteur = largeur * n.get_height() / n.get_width()

    if hauteur > y * 0.7:  # too tall for screen
        largeur = largeur * (y * 0.7) / hauteur  # reduce width to keep ratio
        hauteur = y * 0.7

    image_transformer = pygame.transform.scale(n, (largeur, hauteur))
    return image_transformer


class ecran:
    infoObject = pygame.display.Info()
    size = (infoObject.current_w // 2, infoObject.current_h // 2)
    screen = pygame.display.set_mode(size, pygame.RESIZABLE)


var_x, var_y = ecran.screen.get_width(), ecran.screen.get_height()


class font:
    chemin = "../index/font/Magical Story.ttf"
    font = pygame.font.Font(chemin, 800 // 70)


class text:

    def __init__(self, texte=None, taille=None, sens=None, coo=None):
        self.texte = texte
        self.taille = taille
        self.sens = sens
        self.coo = coo


class particle:

    def __init__(self, taille=None, direction=None, color=None, transparance=None, deplace=None, v=None):
        self.taille = taille  # le ratio de la particle
        self.coo = direction  # l'angle de la droite
        self.color = color
        self.transp = transparance
        self.deplace = deplace  # endroit ou ce situe le point
        self.vitesse = v



class son:
    chemin_whoosh = "../index/son/effect/whoosh1.mp3"
    whoosh = pygame.mixer.Sound(chemin_whoosh)
    volume = 1


class image:
    chemin_carte_dos = "../index/image/fond/dos carte v2.png"
    carte_dos = pygame.image.load(chemin_carte_dos).convert_alpha()


class obj:
    rn = True
    aucun_paquet = True
    liste_particle_click = []


texte_clique = text("Click to OPEN", var_x // 80, -1, (var_x // 2, var_y // 2))  # le sens est -1 decroissan 1 croissant

while obj.rn:

    ecran.screen.fill(couleur(1))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            pygame.mixer.quit()
            pygame.font.quit()
            pygame.quit()

        if event.type == pygame.VIDEORESIZE:
            pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            var_x, var_y = ecran.screen.get_width(), ecran.screen.get_height()
            font.font = pygame.font.Font(font.chemin, 800 // 70)
            texte_clique = text("Click to OPEN", var_x // 80, -1, (var_x // 2, var_y // 2))

    texte_clique_open()
    effect(obj.liste_particle_click, (var_x // 2, var_y // 2))
    pygame.display.flip()
    clock.tick(60)
