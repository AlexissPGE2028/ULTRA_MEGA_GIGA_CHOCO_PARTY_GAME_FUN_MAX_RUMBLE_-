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


def creer_nuage(liste, position, n):
    if obj.wait == 1:
        for i in range(n):
            liste.append(Particle(position, 10, random.randint(10, 20) * 0.3, random.randint(0, 360), None, image.chemin_nuage_effet))
        obj.wait = 0
    else:
        return


def effet_nuage(liste):
    if len(liste) == 0:
        return True
    else:
        for p in liste:
            n = p.radius
            if n > 0:
                p.move()
                p.image.resize((var_x // 100 * p.radius, var_x // 100 * p.radius))
                p.draw()
                n -= 0.3
                p.radius = n
            else:
                liste.remove(p)


def condition_dispawn_booster(pak_booster):
    if pak_booster.n_carte == pak_booster.numero:
        affichageutilte(pak)
        creer_nuage(obj.liste_effect, pak_booster.coo, 50)
        alors = effet_nuage(obj.liste_effect)
        if alors is True:
            return
    else:
        affichageutilte(pak)
        annim_pak(pak_booster)
        pak.image_booster.affiche((var_x // 2, var_y // 2), ecran.screen)


def annim_pak(paket_booster):
    if obj.clic is True:
        if obj.test_pak_annim > 2:
            obj.pak_annim_clic += var_x // 13
            obj.test_pak_annim = 0
            obj.clic = False
        x = obj.pak_annim_clic
        if x > var_x * 11 // 21:
            obj.pak_annim_clic_signe = -1
            obj.test_pak_annim += 1
        if x < var_x // 2:
            obj.pak_annim_clic_signe = 1
            obj.test_pak_annim += 1
            return
        if obj.pak_annim_clic_signe == 1:
            x += 20
            obj.pak_annim_clic = x
            paket_booster.image_booster.resize((x, x))
        else:
            x -= 20
            obj.pak_annim_clic = x
            paket_booster.image_booster.resize((x, x))


def ouvrir_booster(paket_booster):
    i = paket_booster.numero
    print(i)
    if i > paket_booster.n_carte - 1:
        return
    pomme = paket_booster.liste[i]
    angle_rdm = (360 // paket_booster.n_carte) * i
    x = paket_booster.coo[0] + random.randint(var_x//5, var_x//3.5) * math.sin(angle_rdm)
    y = paket_booster.coo[1] + random.randint(var_x//5, var_x//3.5) * math.cos(angle_rdm)
    print(x, y)
    pomme.cooV2 = x, y
    pomme.image.angle = angle_rdm
    paket_booster.numero += 1


def affichageutilte(paket_booster):
    for pomme in paket_booster.liste:
        if pomme.cooV2 is not None:
            pomme.mouvement(20)
            pomme.image.resize((var_x//4, var_x//4))
            pomme.image.affiche(pomme.coo, ecran.screen)


class ecran:
    infoObject = pygame.display.Info()
    size = (infoObject.current_w // 2, infoObject.current_h // 2)
    screen = pygame.display.set_mode(size, pygame.RESIZABLE)


var_x, var_y = ecran.screen.get_width(), ecran.screen.get_height()


class font:
    chemin = None
    font = pygame.font.Font(chemin, 800 // 70)


class image:

    chemin_nuage_effet = "../index/image/rare.png"

    def __init__(self, ymage=None):
        self.ymage = pygame.image.load(ymage)
        self.image_clone = self.ymage
        self.image_zone = None
        self.rect = None
        self.angle = None

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
        self.image_zone = surface_affiche.blit(self.image_clone, self.rect)

    def rotate(self, angle):
        self.image_clone = pygame.transform.rotate(self.image_clone, angle)


class paquet:

    def __init__(self, n_carte=None, coo=None):
        self.n_carte = n_carte
        self.liste = []
        self.coo = coo
        self.image_booster = None
        self.numero = 0

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
        self.cooV2 = None
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

    def mouvement(self, speed, coov2=None):
        if coov2 is None:
            x2, y2 = self.cooV2
        else:
            x2, y2 = coov2 
        x, y = self.coo
        px, py = x, y
        radians = math.atan2(y2 - py, x2 - px)
        distance = math.hypot(x2 - px, y2 - py)
        distance = int(distance)
        if speed > distance:
            return
        dx = math.cos(radians) * speed
        dy = math.sin(radians) * speed
        if distance > 0:
            distance -= 1
            x += dx
            y += dy
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
    def __init__(self, coo, radius, speed, angle, colour=None, image_particle=None):
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
        if image_particle is None:
            self.image = None
        else:
            self.image = image(image_particle)

    def move(self):
        self.x += math.sin(self.angle) * self.speed
        self.y -= math.cos(self.angle) * self.speed
        self.rect.x = int(round(self.x))
        self.rect.y = int(round(self.y))

    def draw(self):
        x = self.x
        y = self.y
        if self.colour is not None:
            pygame.draw.circle(ecran.screen, self.colour, (int(round(x, 0)), int(round(y, 0))), self.radius)
        else:
            self.image.affiche((self.x, self.y), ecran.screen)


class son:
    chemin_whoosh = "../index/son/effect/whoosh1.mp3"
    whoosh = pygame.mixer.Sound(chemin_whoosh)
    volume = 1


class obj:
    rn = True
    aucun_paquet = True
    liste_particle_click = []
    liste_angle = []
    wait = 1
    liste_effect = []
    pak_annim_clic_signe = 1
    pak_annim_clic = var_x // 2
    clic = False
    test_pak_annim = 0


texte_clique = text("Click to OPEN", var_x // 80, -1, (var_x // 2, var_y // 2))  # le sens est -1 decroissan 1 croissant
texte_fps = text(str(clock.get_fps()), var_x // 20, None, (var_x // 40, var_y // 20), (0, 0, 0))

pak = paquet(10, (var_x//2, var_y//2))
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
                if pak.image_booster.image_zone.collidepoint(event.pos):
                    ouvrir_booster(pak)
                    obj.clic = True

    for j in obj.liste_particle_click:
        if len(j[0]) == 1:
            obj.liste_particle_click.remove(j)
        else:
            effect(j[0], j[1])
    texte_fps.show(str(int(clock.get_fps())))
    condition_dispawn_booster(pak)
    pygame.display.flip()
    clock.tick(65)
