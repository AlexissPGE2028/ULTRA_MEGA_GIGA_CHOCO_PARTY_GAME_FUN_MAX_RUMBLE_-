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


def distribu():

    if len(obj.coordonne_generateur) == 0:
        if annim.endistribu == 0:
            for k in range(10):
                coo = random.randint(11 * var_x // 24, 13 * var_x // 24), random.randint(11 * var_y // 24, 13
                                                                                         * var_y // 24)
                obj.coordonne_generateur.append(coo)

    if len(obj.coordonne_generateur_paquet) == 0:
        if annim.endistribu == 0:
            for k in range(10):
                coo = var_x // 2 - 10 * (var_x // 200) + (k * (var_x // 100)), var_y - var_y // 100
                obj.coordonne_generateur_paquet.append(coo)

    if annim.distribu == 0:
        if obj.paquet_en_reserve > 0:
            image_carte = resize(image.carte_dos, (var_x // 3, 10 * var_y // 20))

            for v in obj.coordonne_generateur_paquet:
                image_carte_co = image_carte.get_rect()
                image_carte_co.center = v
                ecran.screen.blit(image_carte, image_carte_co)

    if annim.distribu == 1:
        annim.endistribu = 1

        if obj.k < 1:
            obj.k = 10
            annim.distribu = 0
            annim.endistribu = 0
            obj.paquet_en_reserve -= 1

        if obj.t >= 10:
            obj.t = 0

        if len(carte.liste_carte_afficher) == 0:
            obj.coordonne_generateur_paquet.reverse()
            obj.coordonne_generateur.reverse()

            for p in obj.coordonne_generateur_paquet:
                carte.liste_carte_afficher.append(p)

            for p in obj.coordonne_generateur:
                carte.liste_coo_carte_afficher_prime.append(p)

            obj.coordonne_generateur_paquet.reverse()
            obj.coordonne_generateur.reverse()

        if len(obj.coordonne_generateur_paquet_clone) == 0:
            for p in obj.coordonne_generateur_paquet:
                obj.coordonne_generateur_paquet_clone.append(p)

        if obj.t <= 9:

            image_carte = resize(image.carte_dos, (var_x // 3, 10 * var_y // 20))

            DestinationX = obj.coordonne_generateur[obj.k - 1][0]
            PositionX = carte.liste_carte_afficher[obj.t][0]
            DestinationY = obj.coordonne_generateur[obj.k - 1][1]
            PositionY = carte.liste_carte_afficher[obj.t][1]

            vitesse = 20

            angle = math.atan2((DestinationY - PositionY), (DestinationX - PositionX))

            if (DestinationY - PositionX) < 0:
                PositionX += int(vitesse * math.cos(angle))
                PositionY += int(vitesse * math.sin(angle))

            if (DestinationY - PositionY) > 0:
                obj.coordonne_generateur[obj.k - 1] = PositionX, PositionY

            carte.liste_carte_afficher[obj.t] = PositionX, PositionY

            for v in obj.coordonne_generateur_paquet:
                image_carte_co = image_carte.get_rect()
                image_carte_co.center = v
                ecran.screen.blit(image_carte, image_carte_co)

            if len(carte.liste_carte_afficher) == 10:

                for v in range(0, 9):
                    if carte.liste_carte_afficher[v][1] == obj.coordonne_generateur[9 - v][1]:
                        image_carte_co = image_carte.get_rect()
                        image_carte_co.center = carte.liste_carte_afficher[v]
                        ecran.screen.blit(image_carte, image_carte_co)

                image_carte_co = image_carte.get_rect()
                image_carte_co.center = carte.liste_carte_afficher[obj.t]
                ecran.screen.blit(image_carte, image_carte_co)

            if PositionY != obj.coordonne_generateur_paquet_clone[obj.k - 1][1]:
                if len(obj.coordonne_generateur_paquet) == obj.k:
                    obj.coordonne_generateur_paquet.pop(-1)

            if (DestinationY - PositionY) == 0:
                obj.k -= 1
                obj.t += 1


def anim_carte():
    if annim.distribu == 0:
        distribu()
        if annim.carte_retourne == 0:
            if annim.en_annim_retourneN == 0:
                image_carte = resize(image.carte_dos, (var_x // 3, var_y // 2))

                for v in carte.liste_carte_afficher:
                    image_carte_co = image_carte.get_rect()
                    image_carte_co.center = v

                    ecran.screen.blit(image_carte, image_carte_co)
            else:
                if annim.en_annim_retourne == 0:
                    print("wait")

                else:
                    print("wait")

        else:
            if annim.en_annim_retourne == 0:
                print("wait")

            else:
                print("wait")

    else:
        distribu()


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


class annim:
    carte_retourne = 0      # 0 = carte non retourné  /  1 = carte retourné
    en_annim_retourne = 0   # 0 = non  /  1 = oui
    en_annim_retourneN = 0  # 0 = non  /  1 = oui
    face_en_annim = 0       # 0 = dos  /  1 = face
    distribu = 1            # 0 = non  /  1 = oui
    paquet_en_attente = 0   # 0 = non  /  1 = oui
    endistribu = 0


class carte:

    liste_carte_afficher = []
    liste_coo_carte_afficher_prime = []


class son:
    chemin_whoosh = "../index/son/effect/whoosh1.mp3"
    whoosh = pygame.mixer.Sound(chemin_whoosh)
    volume = 1


class image:
    chemin_carte_dos = "../index/image/fond/dos carte v2.png"
    carte_dos = pygame.image.load(chemin_carte_dos).convert_alpha()


class obj:
    rn = True
    coordonne_generateur = []
    coordonne_generateur_paquet = []
    coordonne_generateur_paquet_clone = []
    k = 10
    t = 0
    ancienne_dim = var_x, var_y
    paquet_en_reserve = 1


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

            obj.coordonne_generateur = []
            obj.coordonne_generateur_paquet = []

            if annim.distribu == 0:
                for j in obj.coordonne_generateur:
                    coos = j[0] + (obj.ancienne_dim[0] - var_x), j[1] + (obj.ancienne_dim[1] - var_y)
                    obj.coordonne_generateur.append(coos)

                for j in obj.coordonne_generateur_paquet:
                    coos = j[0] + (obj.ancienne_dim[0] - var_x), j[1] + (obj.ancienne_dim[1] - var_y)
                    obj.coordonne_generateur_paquet.append(coos)

                if len(carte.liste_carte_afficher) != 0:
                    for j in range(len(carte.liste_carte_afficher)):
                        if var_x - obj.ancienne_dim[0] > 0:
                            carte.liste_carte_afficher[j] = carte.liste_carte_afficher[j][0] * \
                                                            (((var_x - obj.ancienne_dim[0]) / obj.ancienne_dim[0]) + 1), \
                                                            carte.liste_carte_afficher[j][1]
                        if var_x - obj.ancienne_dim[0] < 0:
                            carte.liste_carte_afficher[j] = carte.liste_carte_afficher[j][0] * \
                                                            (1 - ((var_x - obj.ancienne_dim[0]) / obj.ancienne_dim[1])), \
                                                            carte.liste_carte_afficher[j][1]

                        print(((var_x - obj.ancienne_dim[0]) / obj.ancienne_dim[0]) * 100)

                obj.ancienne_dim = var_x, var_y

    anim_carte()

    pygame.display.flip()
    clock.tick(60)