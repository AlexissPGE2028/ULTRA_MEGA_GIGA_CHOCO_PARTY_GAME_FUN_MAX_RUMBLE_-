import pygame
import random

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


def carte():
    font.font_taille = pygame.font.Font(font.chemin, var_x // 40)
    texte = font.font_taille.render(objet.ecrie, True, couleur(1))
    texte_rarete = font.font_taille.render(random_nom.liste_nom[objet.choix], True, couleur(1))

    texte_rect = texte.get_rect()
    texte_rect_rare = texte_rarete.get_rect()

    bonne_image = image.dos_carte_new
    image.dos_carte_ = bonne_image

    texte_rect.center = var_x // 2, var_y * 8 // 10
    texte_rect_rare.center = var_x // 2, var_y * 8.5 // 10

    dos_carte_co = image.dos_carte_.get_rect()
    dos_carte_co.center = var_x // 2, var_y // 2

    if cartes.retourne is False:
        if objet.annim is True:
            if cartes.phase == 1:

                largeur = var_y // 3
                hauteur = largeur * bonne_image.get_height() / bonne_image.get_width()

                if hauteur > (var_y * 8 // 10) * 0.8:  # too tall for screen
                    largeur = largeur * ((var_y * 8 // 10) * 0.8) / hauteur  # reduce width to keep ratio
                    hauteur = (var_y * 8 // 10) * 0.8

                image.dos_carte_ = pygame.transform.scale(image.dos_carte_, (largeur, hauteur))

                calcul_x = image.dos_carte_.get_width() - (var_x // 50)

                if calcul_x > 0:
                    image.dos_carte_ = pygame.transform.scale(image.dos_carte_, (calcul_x, hauteur))
                    dos_carte_co = image.dos_carte_.get_rect()
                    dos_carte_co.center = var_x // 2, var_y // 2
                    ecran.screen.blit(image.dos_carte_, dos_carte_co)

                else:
                    cartes.phase = 2
                    objet.annim_valeur = 1
                    image.image_contour_choix = image.liste_image_carte[objet.choix]
                    image.image_contour_choix = pygame.transform.scale(image.image_contour_choix, (1, var_y * 8
                                                                                                   // 10))
                    image.dos_carte_ = pygame.transform.scale(image.dos_carte, (var_x // 3, var_y * 8 // 10))

            else:
                calcul_x_carte = image.image_contour_choix.get_width() + (var_x // 50)
                font.annim = font.annim + 2

                objet.annim_valeur += 1
                if calcul_x_carte < var_x // 3:
                    image.image_contour_choix = pygame.transform.scale(image.liste_image_carte[objet.choix], (
                        calcul_x_carte, var_y * 8 // 10))
                    carte_contour_co = image.image_contour_choix.get_rect()
                    carte_contour_co.center = var_x // 2, var_y // 2

                    font.font_taille = pygame.font.Font(font.chemin, font.annim)

                    texte = font.font_taille.render(objet.ecrie, True, couleur(1))
                    texte_rarete = font.font_taille.render(random_nom.liste_nom[objet.choix], True, couleur(1))

                    texte_rect = texte.get_rect()
                    texte_rect_rare = texte_rarete.get_rect()

                    texte_rect.center = var_x // 2, var_y * 8 // 10
                    texte_rect_rare.center = var_x // 2, var_y * 8.5 // 10

                    ecran.screen.blit(image.image_contour_choix, carte_contour_co)
                    ecran.screen.blit(texte, texte_rect)
                    ecran.screen.blit(texte_rarete, texte_rect_rare)

                else:
                    cartes.phase = 3
                    objet.annim = False
                    cartes.retourne = True
                    cartes.part = False

                    image.image_contour_choix = image.liste_image_carte[objet.choix]
                    image.image_contour_choix = pygame.transform.scale(image.image_contour_choix, (var_x // 3, var_y
                                                                                                   * 8 // 10))
                    carte_contour_co = image.image_contour_choix.get_rect()
                    carte_contour_co.center = var_x // 2, var_y // 2
                    ecran.screen.blit(image.image_contour_choix, carte_contour_co)
                    ecran.screen.blit(texte, texte_rect)
                    ecran.screen.blit(texte_rarete, texte_rect_rare)

                    font.annim = 1

            return None

        else:
            dos_carte_co = image.dos_carte_.get_rect()
            dos_carte_co.center = var_x // 2, var_y // 2
            click = ecran.screen.blit(image.dos_carte_, dos_carte_co)

            return click

    if cartes.retourne is True:
        if cartes.part is False:
            image.image_contour_choix = image.liste_image_carte[objet.choix]
            image.image_contour_choix = pygame.transform.scale(image.image_contour_choix, (var_x // 3, var_y
                                                                                           * 8 // 10))
            carte_contour_co = image.image_contour_choix.get_rect()
            carte_contour_co.center = var_x // 2, var_y // 2
            click = ecran.screen.blit(image.image_contour_choix, carte_contour_co)
            ecran.screen.blit(texte, texte_rect)
            ecran.screen.blit(texte_rarete, texte_rect_rare)

            return click

        if cartes.part is True:

            image.dos_carte_ = pygame.transform.scale(bonne_image, (var_x // 3, var_y * 8 // 10))
            dos_carte_co = image.dos_carte_.get_rect()
            dos_carte_co.center = var_x // 2, var_y // 2
            ecran.screen.blit(image.dos_carte_, dos_carte_co)

            if objet.annim_valeur <= var_x // 2 + var_x // 6:

                x = var_x // 2 + objet.annim_valeur
                carte_contour_co = image.image_contour_choix.get_rect()

                carte_contour_co.center = x, var_y // 2
                texte_rect.center = x, var_y * 8 // 10
                texte_rect_rare.center = x, var_y * 8.5 // 10

                ecran.screen.blit(image.image_contour_choix, carte_contour_co)
                ecran.screen.blit(texte, texte_rect)
                ecran.screen.blit(texte_rarete, texte_rect_rare)
                objet.annim_valeur += var_x // 10
            else:
                objet.annim_valeur = 0
                cartes.retourne = False
                cartes.phase = 0


def fond_graphique():

    if cartes.fond >= 0:
        if cartes.fond > 7:
            cartes.fond = 0
        print(cartes.fond)

        image.image_fond_graphique = image.dos_carte_new

        largeur = var_y // 3
        hauteur = largeur * image.image_fond_graphique.get_height() / image.image_fond_graphique.get_width()

        if hauteur > (var_y * 8 // 10) * 0.8:  # too tall for screen
            largeur = largeur * ((var_y * 8 // 10) * 0.8) / hauteur  # reduce width to keep ratio
            hauteur = (var_y * 8 // 10) * 0.8

        image.image_fond_graphique = pygame.transform.scale(image.image_fond_graphique, (largeur, hauteur))
        fond_co = image.image_fond_graphique.get_rect()
        fond_co.center = var_x // 2, var_y // 2
        ecran.screen.blit(image.image_fond_graphique, fond_co)


def boucle():
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    for k in range(100):
        for i in range(100):
            choix = int(random.choice(random_nom.choix))
            if choix == 0:
                a += 1
            if choix == 1:
                b += 1
            if choix == 2:
                c += 1
            if choix == 3:
                d += 1
            if choix == 4:
                e += 1
            if choix == 5:
                f += 1
    print(a / 100, b / 100, c / 100, d / 100, e / 100, f / 100)


class ecran:
    infoObject = pygame.display.Info()
    size = (infoObject.current_w // 2, infoObject.current_h // 2)
    screen = pygame.display.set_mode(size, pygame.RESIZABLE)


class random_nom:
    liste_chemin = ["../index/fichier/sourire_commun.txt", "../index/fichier/sourire_noncommun.txt",
                    "../index/fichier/sourire_rare.txt", "../index/fichier/sourire_epique.txt",
                    "../index/fichier/sourire_legendaire.txt", "../index/fichier/sourire_godess.txt"]

    liste_nom = ["commun", "non-commun", "rare", "épique", "légendaire", "GODESS"]

    choix = "0" * 1000 + "1" * 500 + "2" * 250 + "3" * 125 + "4" * 60 + "5" * 30

    fichier = open("../index/fichier/sourire_commun.txt", "r", encoding="UTF-8")
    fichier = fichier.read()
    sourire = fichier.split("\n")


class image:
    chemin_dos_carte = "../index/image/sourire dos de carte.png"
    chemin_commun = "../index/image/commun.png"
    chemin_uncommun = "../index/image/noncommun.png"
    chemin_rare = "../index/image/rare.png"
    chemin_epic = "../index/image/epic.png"
    chemin_legendaire = "../index/image/legendaire.png"
    chemin_godess = "../index/image/godess.png"

    chemin_dos_carte_new = "../index/image/fond/dos carte v2.png"

    dos_carte_new = pygame.image.load(chemin_dos_carte_new).convert_alpha()

    dos_carte = pygame.image.load(chemin_dos_carte).convert_alpha()
    commun = pygame.image.load(chemin_commun).convert_alpha()
    uncommun = pygame.image.load(chemin_uncommun).convert_alpha()
    rare = pygame.image.load(chemin_rare).convert_alpha()
    epic = pygame.image.load(chemin_epic).convert_alpha()
    legendaire = pygame.image.load(chemin_legendaire).convert_alpha()
    godess = pygame.image.load(chemin_godess).convert_alpha()

    dos_carte_ = pygame.transform.scale(dos_carte, (ecran.screen.get_width() // 3, ecran.screen.get_height() * 8 // 10))
    commun_ = pygame.transform.scale(commun, (ecran.screen.get_width() // 3, ecran.screen.get_height() * 8 // 10))
    uncommun_ = pygame.transform.scale(uncommun, (ecran.screen.get_width() // 3, ecran.screen.get_height() * 8 // 10))
    rare_ = pygame.transform.scale(rare, (ecran.screen.get_width() // 3, ecran.screen.get_height() * 8 // 10))
    epic_ = pygame.transform.scale(epic, (ecran.screen.get_width() // 3, ecran.screen.get_height() * 8 // 10))
    legendaire_ = pygame.transform.scale(legendaire, (ecran.screen.get_width() // 3, ecran.screen.get_height() * 8
                                                      // 10))
    godess_ = pygame.transform.scale(godess, (ecran.screen.get_width() // 3, ecran.screen.get_height() * 8 // 10))

    liste_image_carte = [commun_, uncommun_, rare_, epic_, legendaire_, godess_]

    image_contour_choix = liste_image_carte[0]
    image_fond_graphique = None


class font:
    chemin = "../index/font/Magical Story.ttf"
    font = pygame.font.Font(chemin, 800 // 70)
    annim = 1


class objet:
    rn = True
    ecrie = random.choice(random_nom.sourire)
    choix = 0
    annim = False
    annim_valeur = 1
    valeur_verif = 0


class son:
    chemin_whoosh = "../index/son/effect/whoosh1.mp3"
    whoosh = pygame.mixer.Sound(chemin_whoosh)
    volume = 1


class cartes:
    retourne = False
    phase = 3
    part = False
    fond = 0


var_x, var_y = ecran.screen.get_width(), ecran.screen.get_height()
epl_carte = carte()

while objet.rn:

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

            image.dos_carte_ = pygame.transform.scale(image.dos_carte, (var_x // 3, var_y * 8 // 10))
            image.commun_ = pygame.transform.scale(image.commun,
                                                   (ecran.screen.get_width() // 3, ecran.screen.get_height() * 8 // 10))
            image.uncommun_ = pygame.transform.scale(image.uncommun,
                                                     (ecran.screen.get_width() // 3, ecran.screen.get_height() * 8
                                                      // 10))
            image.rare_ = pygame.transform.scale(image.rare, (ecran.screen.get_width() // 3, ecran.screen.get_height()
                                                              * 8 // 10))
            image.epic_ = pygame.transform.scale(image.epic, (ecran.screen.get_width() // 3, ecran.screen.get_height()
                                                              * 8 // 10))
            image.legendaire_ = pygame.transform.scale(image.legendaire,
                                                       (ecran.screen.get_width() // 3, ecran.screen.get_height() * 8
                                                        // 10))
            image.godess_ = pygame.transform.scale(image.godess,
                                                   (ecran.screen.get_width() // 3, ecran.screen.get_height() * 8 // 10))
            image.liste_image_carte = [image.commun_, image.uncommun_, image.rare_, image.epic_, image.legendaire_,
                                       image.godess]

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if epl_carte is not None:
                    if epl_carte.collidepoint(event.pos):

                        if cartes.phase == 1 or cartes.phase == 2:
                            objet.choix = int(random.choice(random_nom.choix))

                            fichier = open(random_nom.liste_chemin[objet.choix], "r", encoding="UTF-8")
                            fichier = fichier.read()
                            random_nom.sourire = fichier.split("\n")
                            print(objet.choix)

                            objet.ecrie = random.choice(random_nom.sourire)
                            pygame.display.set_caption(objet.ecrie)

                            objet.annim = True
                            cartes.retourne = False

                            cartes.phase = 1
                            cartes.fond += 1

                        if cartes.phase == 3:
                            cartes.part = True
                            cartes.phase = 2
                            son.whoosh.play()
                            son.whoosh.set_volume(son.volume)

    fond_graphique()
    epl_carte = carte()

    pygame.display.flip()
    clock.tick(80)
