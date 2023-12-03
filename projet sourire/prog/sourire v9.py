import pygame  # moteur de jeu
import random  # inclue le hasard
import math    # pour tout les calcul de deplacement dans le plan

pygame.init()       # initialisation
pygame.mixer.init()
pygame.font.init()

clock = pygame.time.Clock()     # pour controler les fps
pygame.display.set_caption("Sourire")


def couleur(n):     # vielle fontion recuperer dans le programme cepe cliqueur
    """permet le choix d'une couleur dans la liste suivante"""
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


def texte_clique_open():    # fontion inutiliser
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


def calcul_new_itineraire(coo, paket):  # permet un effet graphique des cartes en "decalé"
    if coo == paket.liste[0].cooV2:
        return
    for numero in range(len(paket.liste)):
        if numero == 0:
            x, y = coo
            x -= numero * 4
            y += numero * 4
            coo = x, y
            paket.liste[numero].cooV2 = coo
        else:
            coo = paket.liste[numero - 1].cooV2
            x, y = coo
            x -= 6
            y += 3
            coo = x, y
            paket.liste[numero].cooV2 = coo


def rangement_carte(paket):     # fontion permetant l'affichage graphique de la fonction au dessus
    calcul_new_itineraire(((var_x // 2) + 40, (var_y // 2) - 40), paket)
    affichageutilte(paket, 0.5)
    cart = paket.liste[0]
    if cart.coo[0] >= cart.cooV2[0] - 1:
        obj.systeme_range_carte = None
        return True


def dernier_carte_effect_cool(paket, index):     # fonction en attente de reconstruction
    cart = paket.liste[index]
    n = obj.maxi_revel
    print(n)
    if n == 10:
        cart.reverse = True
    if cart.reverse is False:
        x = cart.image_dos.image_clone.get_width()
        y = cart.image_dos.image_clone.get_height()
        x2 = x - 2 * n
        size = x2, y
        if x2 < 0:
            cart.reverse = None
            cart.image.resize((var_x // 4, var_x // 4))
            cart.image.resize_moche((x, var_x // 4))
            obj.maxi_revel += 1
            return
        cart.image_dos.resize_moche(size)
        cart.image_dos.affiche(cart.cooV2, ecran.screen)
    elif cart.reverse is None:
        x = cart.image.image_clone.get_width()
        y = cart.image.image_clone.get_height()
        x2 = x + 2 * n
        size = x2, y
        if x2 >= cart.image.size_original[0]:
            cart.reverse = "none2"
            cart.image.resize((var_x // 4, var_x // 4))
            cart.image.resize_moche((x, var_x // 4))
            obj.maxi_revel += 1
            return
        cart.image.resize_moche(size)
        cart.image.affiche(cart.cooV2, ecran.screen)
    elif cart.reverse == "none2":
        x = cart.image.image_clone.get_width()
        y = cart.image.image_clone.get_height()
        x2 = x - 2 * n
        size = x2, y
        if x2 < 0:
            cart.reverse = "none3"
            cart.image_dos.resize((var_x // 4, var_x // 4))
            cart.image_dos.resize_moche((x, var_x // 4))
            obj.maxi_revel += 1
            return
        cart.image_dos.resize_moche(size)
        cart.image_dos.affiche(cart.cooV2, ecran.screen)
    elif cart.reverse == "none3":
        x = cart.image_dos.image_clone.get_width()
        y = cart.image_dos.image_clone.get_height()
        x2 = x + 2 * n
        size = x2, y
        if x2 >= cart.image.size_original[0]:
            cart.reverse = False
            cart.image_dos.resize((var_x // 4, var_x // 4))
            cart.image_dos.resize_moche((x, var_x // 4))
            obj.maxi_revel += 1
            return
        cart.image_dos.resize_moche(size)
        cart.image_dos.affiche(cart.cooV2, ecran.screen)
    else:
        x = cart.image.image_clone.get_width()
        y = cart.image.image_clone.get_height()
        x += 2 * n
        size = x, y
        if x >= cart.image.size_original[0]:
            obj.image_a_clic = cart.image.image_zone
            cart.image.affiche(cart.cooV2, ecran.screen)
            return True
        cart.image.resize_moche(size)
        cart.image.affiche(cart.cooV2, ecran.screen)


def switch_carte(cart):
    if obj.angle is None:
        obj.angle = random.randint(0, 360)
        x = cart.coo[0] + var_x * math.sin(obj.angle)
        y = cart.coo[1] + var_x * math.cos(obj.angle)
        cart.cooV2 = x, y
        son.whoosh.play()
        son.whoosh.set_volume(son.volume)
    else:
        return True


def clic_carte_revel(paket):    # permet la revelation des cartes du paquet (fontion un peu spaguettie a réécrire)
    affiche(paket)
    index = len(paket.liste)-1
    if index < 0:
        return
    cart = paket.liste[index]
    obj.image_a_clic = cart.image_dos.image_zone
    if obj.clic_revel is True:
        fini = cart.revel_carte(0.5)
        if fini is True:
            texte = text(None, 80, None, (500, 500), (0, 0, 0))
            texte.show(cart.rare)
            obj.coo_carte_enquestion = cart.cooV2
            obj.systeme_revelV2 = True
            if obj.clic_revelV2 is True:
                ok = switch_carte(cart)
                if ok is True:
                    okre = cart.mouvement(0.1)
                    cart.image.affiche(cart.coo, ecran.screen)
                    if okre is True:
                        paket.liste.remove(cart)
                        paket.numero += 1
                        obj.clic_revelV2 = False
                        obj.systeme_revelV2 = False
                        obj.clic_revel = False
                        obj.angle = None


def affiche(paket):     # fontion d'affichage, cette fontion est a implanter dans l'objet "paquet"
    for k in paket.liste:
        k.image_dos.affiche(k.cooV2, ecran.screen)


def effect(liste, position):    # fonctio inutiliser pour faire des effet de particule
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
            p.move(1)
            p.draw()

            # partie affichage
            n -= 0.1
            p.radius = n
        else:
            liste.remove(p)


def creer_nuage(liste, position, n):    # fonction permetant de créé des particule a partir d'image
    if obj.wait == 1:
        for i in range(n):
            liste.append(Particle(position, 8, random.randint(10, 20) * 0.3, random.randint(0, 360), None,
                                  image.chemin_nuage_effet, 0.5))
            obj.liste_effect = liste
        obj.wait = 0
    else:
        return


def effet_nuage(liste):     # fontion affichant les particule créé precedement
    if len(liste) == 0:
        obj.wait = 1
        return True
    else:
        for p in liste:
            n = p.radius
            if n > 0:
                p.move()
                p.image.resize((var_x // 100 * p.radius, var_x // 100 * p.radius))
                p.draw()
                distance = n
                letemps = p.temps * obj.fps
                speed = distance / letemps
                if p.speedV2 is None:
                    p.speedV2 = speed
                n -= p.speedV2
                p.radius = n
            else:
                liste.remove(p)


def condition_dispawn_booster(pak_booster):     # fonction gerant plusieur effet relatif au paquet et aux cartes
    if pak_booster.n_carte == pak_booster.numero:
        fini = affichageutilte(pak, 0.1)
        creer_nuage(obj.liste_effect, pak_booster.coo, 50)
        fini2 = effet_nuage(obj.liste_effect)
        if fini is True and fini2 is True:
            return True
    else:
        affichageutilte(pak, 0.2)
        annim_pak(pak_booster)
        pak.image_booster.affiche((var_x // 2, var_y // 2), ecran.screen)

    return False


def annim_pak(paket_booster):   # fontion spaguetie a réécrire permetant un effet sur le paquet
    if obj.clic is True:
        if obj.test_pak_annim > 2:
            obj.pak_annim_clic += var_x // 61
            obj.test_pak_annim = 0
            obj.clic = False
        x = obj.pak_annim_clic
        if x > var_x * 61 // 180:
            obj.pak_annim_clic_signe = -1
            obj.test_pak_annim += 1
        if x < var_x // 3:
            obj.pak_annim_clic_signe = 1
            obj.test_pak_annim += 1
            return
        if obj.pak_annim_clic_signe == 1:
            x += 5
            obj.pak_annim_clic = x
            paket_booster.image_booster.resize((x, x))
        else:
            x -= 5
            obj.pak_annim_clic = x
            paket_booster.image_booster.resize((x, x))


def ouvrir_booster(paket_booster):  # fontion permentant de calculer les coo des cartes lors d'un clic sur le paquet
    i = paket_booster.numero
    if i > paket_booster.n_carte - 1:
        return
    pomme = paket_booster.liste[i]
    angle_rdm = (360 // paket_booster.n_carte) * i
    x = paket_booster.coo[0] + random.randint(var_x//5, var_x//3.5) * math.sin(angle_rdm)
    y = paket_booster.coo[1] + random.randint(var_x//5, var_x//3.5) * math.cos(angle_rdm)
    pomme.cooV2 = x, y
    pomme.image.angle = angle_rdm
    paket_booster.numero += 1


def affichageutilte(paket_booster, letemps):  # fontion permetant d'afficher et de redimentionner les carte (a corriger)
    for pomme in paket_booster.liste:
        if pomme.cooV2 is not None:
            pomme.mouvement(letemps)
            pomme.image_dos.resize((var_x//4, var_x//4))
            pomme.image_dos.affiche(pomme.coo, ecran.screen)
    if paket_booster.liste[len(paket_booster.liste)-1].cooV2 is not None:
        if paket_booster.liste[len(paket_booster.liste)-1].mouvement(letemps) is True:
            return True


class ecran:    # class contenant les info de la fenetre de l'app
    infoObject = pygame.display.Info()
    size = (infoObject.current_w // 1, infoObject.current_h // 1)
    screen = pygame.display.set_mode(size, pygame.RESIZABLE)


var_x, var_y = ecran.screen.get_width(), ecran.screen.get_height()


class font:     # fontion pour ecrire du text
    chemin = None
    font = pygame.font.Font(chemin, 800 // 70)


class image:   # class image, créé des obj image avec plusieur methode

    chemin_nuage_effet = "../index/image/rare.png"

    def __init__(self, ymage=None):
        try:
            self.ymage = pygame.image.load(ymage).convert_alpha(ecran.screen)   # image d'origine qui sert de base
        except:
            print(ymage)
            self.ymage = pygame.image.load("../index/image/image commun/chocolatine.jpg").convert_alpha(ecran.screen)
        self.image_clone = self.ymage   # image totalement modifiable
        self.image_zone = None
        self.rect = None
        self.angle = None
        self.size_original = None

    def resize(self, size):     # redimentionne l'image avec un ratio pour eviter toute distortion
        x, y = size
        largeur = x
        hauteur = largeur * self.ymage.get_height() / self.ymage.get_width()
        if hauteur > y * 0.9:  # too tall for screen
            largeur = largeur * (y * 0.9) / hauteur  # reduce width to keep ratio
            hauteur = y * 0.9
        self.image_clone = pygame.transform.scale(self.ymage, (largeur, hauteur))
        self.size_original = self.image_clone.get_width(), self.image_clone.get_height()

    def affiche(self, coo, surface_affiche):    # permet l'affichage des cartes
        self.rect = self.image_clone.get_rect()
        self.rect.center = coo
        self.image_zone = surface_affiche.blit(self.image_clone, self.rect)

    def rotate(self, angle):    # permet de tourner l'image
        self.image_clone = pygame.transform.rotate(self.image_clone, angle)

    def resize_moche(self, size):   # permet une redimention sans ratio, donc permet la distortion d'image
        self.image_clone = pygame.transform.scale(self.ymage, size)


class paquet:   # class paquet, creer un obj paquet

    def __init__(self, n_carte=None, coo=None):
        self.n_carte = n_carte
        self.liste = []     # liste contenant les obj cartes
        self.coo = coo
        self.image_booster = None
        self.numero = 0

    def creer_carte(self):  # permet de creer les obj cartes et de les stoker dans une liste
        for i in range(self.n_carte):
            karte = carte(i, self.coo)
            karte.rarete()
            karte.chemin_carte()
            print(karte.image_chemin)
            self.liste.append(karte)

    def image_packet(self):     # choisis une image rdm  parmie une liste dans un fichier text
        chemin = "../index/chemin_image/image booster.txt"
        with open(chemin, 'r') as file:
            lire = file.read()
            ligne = lire.split("\n")
            choix = random.choice(ligne)
            self.image_booster = image(choix)
            file.close()


class carte:    # class carte creer des obj carte

    def __init__(self, index=None, coo=None):
        chemin_carte_dos = "../index/image/fond/dos carte v2.png"   # a modifier
        self.index = index
        self.rare = None
        self.image_chemin = None
        self.id = None
        self.coo = coo      # les coo de l'endroit ou ce trouve l'obj
        self.cooV2 = None   # les coo de l'encroit ou dois allez l'obj
        self.image = None   # image de la carte chosis
        self.image_dos = image(chemin_carte_dos)    # image du dos de la carte
        self.reverse = False    # savoir si la carte et retourner ou non
        self.speed = None
        self.color = None

    def rarete(self):   # methode choisisant rdm la valeur de la carte
        random_rare = "0" * 30 + "1" * 20 + "2" * 10 + "3" * 7 + "4" * 5 + "5" * 3
        dico_rare = {"0": "commun",
                     "1": "un-commun",
                     "2": "rare",
                     "3": "epic",
                     "4": "legendaire",
                     "5": "Godess"}
        self.rare = dico_rare[random.choice(random_rare)]

    def chemin_carte(self):     # methode choissant une carte rdm dans un fichier text
        chemin = '../index/chemin_image/' + self.rare + '.txt'
        with open(chemin, 'r') as file:
            lire = file.read()
            ligne = lire.split("\n")
            rdom = random.choice(ligne)
            splitRDom = rdom.split("#")
            self.image_chemin = splitRDom[0]
            try:
                self.id = splitRDom[1]
            except:
                self.id = 0;
            file.close()
            self.image = image(self.image_chemin)

    def mouvement(self, temps, coov2=None):     # permet de calculer le deplacement

        letemps = temps * obj.fps
        if coov2 is None:
            x2, y2 = self.cooV2
        else:
            x2, y2 = coov2 
        x, y = self.coo
        px, py = x, y
        radians = math.atan2(y2 - py, x2 - px)
        distance = math.hypot(x2 - px, y2 - py)
        distance = int(distance)
        speed = distance / letemps
        if self.speed is None:
            self.speed = speed
        if self.cooV2 == self.coo:
            self.speed = None
            return True
        if self.speed > distance:
            self.speed = distance // 2
        dx = math.cos(radians) * self.speed
        dy = math.sin(radians) * self.speed
        if distance > 0:
            distance -= 1
            x += dx
            y += dy
        self.coo = x, y
        if distance == 0:
            self.coo = self.cooV2

    def revel_carte(self, temps):      # methode permetant de revel la carte (effet graphique)
        if self.reverse is False:
            x, y = self.image_dos.image_clone.get_width(), self.image_dos.image_clone.get_height()
            distance = self.image_dos.image_clone.get_width() - 1
            letemps = temps * obj.fps
            if self.speed is None:
                speed = distance / letemps
                self.speed = speed
            calcul = x - self.speed
            if self.speed > x:
                calcul = 1
            if calcul == 1:
                self.reverse = True
                self.image.resize((var_x//4, var_x//4))
                self.image.resize_moche((calcul, self.image.size_original[1]))
            self.image_dos.resize_moche((calcul, y))
            self.image_dos.affiche(self.cooV2, ecran.screen)
        else:
            x, y = self.image.image_clone.get_width(), self.image.image_clone.get_height()
            distance = self.image.size_original[0] - x
            if distance == 0:
                self.image.affiche(self.cooV2, ecran.screen)
                obj.image_a_clic = self.image.rect
                self.speed = None
                return True
            calcul = x + self.speed
            if calcul > self.image.size_original[0]:
                calcul = self.image.size_original[0]
            self.image.resize_moche((calcul, y))
            self.image.affiche(self.cooV2, ecran.screen)


class text:     # class text creant des obj text

    def __init__(self, texte=None, taille=None, sens=None, coo=None, color=None):
        self.texte = texte
        self.taille = taille
        self.sens = sens
        self.coo = coo
        self.color = color

    def show(self, letexte):    # affiche le texte
        font_taille = pygame.font.Font(font.chemin, self.taille)
        texte = font_taille.render(letexte, True, self.color)
        texte_rect = texte.get_rect()
        texte_rect.center = self.coo
        ecran.screen.blit(texte, texte_rect)


class Particle:     # class particule creant des particule
    def __init__(self, coo, radius, speed, angle, colour=None, image_particle=None, temps=None):
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
        self.temps = temps
        self.speedV2 = None
        if image_particle is None:
            self.image = None
        else:
            self.image = image(image_particle)

    def move(self):     # fais bouger ces particule dans l'angle correspondant
        self.x += math.sin(self.angle) * self.speed
        self.y -= math.cos(self.angle) * self.speed
        self.rect.x = int(round(self.x))
        self.rect.y = int(round(self.y))

    def draw(self):     # pour afficher si c'est un image ou créé les particule
        x = self.x
        y = self.y
        if self.colour is not None:
            pygame.draw.circle(ecran.screen, self.colour, (int(round(x, 0)), int(round(y, 0))), self.radius)
        else:
            self.image.affiche((self.x, self.y), ecran.screen)


class son:      # class son
    chemin_whoosh = "../index/son/effect/whoosh1.mp3"
    whoosh = pygame.mixer.Sound(chemin_whoosh)
    volume = 1


class obj:      # class poubelle avec toute les variable utile dans pour tout le programme
    rn = True
    aucun_paquet = True
    liste_particle_click = []
    liste_angle = []
    wait = 1
    liste_effect = []
    pak_annim_clic_signe = 1
    pak_annim_clic = var_x // 3
    clic = False
    test_pak_annim = 0
    systeme_range_carte = False
    systeme_revel = False
    systeme_revelV2 = False
    clic_revel = False
    clic_revelV2 = False
    image_a_clic = None
    maxi_revel = 1
    fps = 140
    angle = None


texte_clique = text("Click to OPEN", var_x // 80, -1, (var_x // 2, var_y // 2))  # le sens est -1 decroissan 1 croissant
texte_fps = text(str(clock.get_fps()), var_x // 20, None, (var_x // 40, var_y // 20), (0, 0, 0))

pak = paquet(10, (var_x//2, var_y//2))
pak.image_packet()
pak.image_booster.resize((var_x // 3, var_x // 3))
pak.creer_carte()
while obj.rn:   # boucle principale

    ecran.screen.fill(couleur(1))

    events = pygame.event.get()
    for event in events:

        if event.type == pygame.QUIT:
            obj.rn = False

        if event.type == pygame.VIDEORESIZE:
            pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            var_x, var_y = ecran.screen.get_width(), ecran.screen.get_height()
            font.font = pygame.font.Font(font.chemin, 800 // 70)
            texte_clique = text("Click to OPEN", var_x // 80, -1, (var_x // 2, var_y // 2))
            pak.image_booster.resize((var_x // 3, var_x // 3))
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if pak.image_booster.image_zone.collidepoint(event.pos):
                    if obj.systeme_range_carte is False:
                        ouvrir_booster(pak)
                        obj.clic = True
                if obj.systeme_revel is True:
                    if obj.image_a_clic.collidepoint(event.pos):
                        obj.clic_revel = True
                if obj.systeme_revelV2 is True:
                    if obj.image_a_clic.collidepoint(event.pos):
                        obj.clic_revelV2 = True

    for j in obj.liste_particle_click:
        if len(j[0]) == 1:
            obj.liste_particle_click.remove(j)
        else:
            effect(j[0], j[1])
    texte_fps.show(str(int(clock.get_fps())))
    if obj.systeme_range_carte is False:
        obj.systeme_range_carte = condition_dispawn_booster(pak)
    if obj.systeme_range_carte is True:
        pak.numero = 0
        obj.systeme_revel = rangement_carte(pak)
    if obj.systeme_revel is True:
        clic_carte_revel(pak)
    pygame.display.update()
    clock.tick(obj.fps)

pygame.mixer.quit()
pygame.font.quit()
pygame.quit()
