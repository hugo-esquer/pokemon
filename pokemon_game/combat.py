import random
import json
import pygame
from models.pokemon import pokemon


class combat():
    def __init__(self, fenetre, joueur):
        self.fenetre = fenetre
        self.pokemon_joueur = joueur
        self.adversaire = None
        self.key_adversaire = None
        self.background = None
        self.NOIR = (0, 0, 0)

        # chargement des assets
        self.barre_ennemi = pygame.image.load("pokemon_game/images/Barre-ennemi.png")
        self.barre_ennemi = pygame.transform.scale(self.barre_ennemi, (282, 78))
        self.barre_joueur = pygame.image.load("pokemon_game/images/Barre-joueur.png")
        self.barre_joueur = pygame.transform.scale(self.barre_joueur, (282, 78))
        self.ouiNon = pygame.image.load("pokemon_game/images/Barre-message-ouinon.png")
        self.ouiNon = pygame.transform.scale(self.ouiNon, (124, 84))
        self.fleche = pygame.image.load("pokemon_game/images/Fleche.png")
        self.fleche = pygame.transform.scale(self.fleche, (14, 20))
        self.police_texte = pygame.font.Font("pokemon_game/typographie/BOMBARD_.ttf", 20)

        # definitino des variables
        self.texte_nom_adversaire = None
        self.niveau_adversaire = None
        self.gagnant = None

        # definition des options pour rejouer ou non
        self.options = ["Oui", "Non"]
        self.option_selectionnee = 0

        #barres de vie
        self.VERT = (0, 255, 0)
        self.adversaire_pv_max = None

        # initialisation de l'objet pokemon du joueur
        with open("pokemon_game/pokemon.json") as mon_fichier:
            data = json.load(mon_fichier)
        dico_joueur = data[self.pokemon_joueur]
        self.joueur = pokemon(dico_joueur["nom"], dico_joueur["pv"], dico_joueur["initiative"],dico_joueur["lvlEvolve"], dico_joueur["evolution"], dico_joueur["type"], dico_joueur["attaque"], dico_joueur["defense"])
        self.sprite_joueur = pygame.image.load(dico_joueur["dos"])
        self.sprite_joueur = pygame.transform.scale(self.sprite_joueur, (160, 160))

        self.texte_nom_joueur = self.police_texte.render(self.joueur.nom.upper(), True, self.NOIR)
        self.joueur_pv_max = self.joueur.pv
        self.choix_adversaire()

    # choix de l'adversaire aléatoire
    def choix_adversaire(self):
        # mise a jour des pv du joueur en cas de nouveau combat
        self.joueur_pv_max = self.joueur.pv

        # choix aléatoire de l'adversaire et initialisation de l'objet pokemon de l'adversaire
        with open("pokemon_game/pokemon.json") as mon_fichier:
            data = json.load(mon_fichier)
        self.key_adversaire = random.choice(list(data.keys()))
        dico_adv = data[self.key_adversaire]
        self.adversaire = pokemon(dico_adv["nom"], dico_adv["pv"], dico_adv["initiative"],dico_adv["lvlEvolve"], dico_adv["evolution"], dico_adv["type"], dico_adv["attaque"], dico_adv["defense"])
        self.sprite_adversaire = pygame.image.load(dico_adv["face"])
        self.sprite_adversaire = pygame.transform.scale(self.sprite_adversaire, (160, 160))
        self.texte_nom_adversaire = self.police_texte.render(self.adversaire.nom.upper(), True, self.NOIR)

        # ajustement du niveau de l'adversaire en fonction du niveau du joueur
        level = 0
        if self.joueur.lvl == 1 or self.joueur.lvl == 2:
            level = random.randint(1, self.joueur.lvl + 2)
        else:
            level = random.randint(self.joueur.lvl - 2, self.joueur.lvl + 2)
        i = 1
        while i < level:
            self.adversaire.gain_lvl()
            i += 1
        # mise a jour de la variable pv_max de l'adversaire pour l'affichage de la barre de vie
        self.adversaire_pv_max = self.adversaire.pv

        self.niveau_adversaire = self.police_texte.render(str(self.adversaire.lvl), True, self.NOIR)

        # choix du background en fonction du type de l'adversaire
        if self.adversaire.type == "eau":
            self.background = pygame.image.load("pokemon_game/images/BG-Eau.png")
            self.background = pygame.transform.scale(self.background, (800, 480))
        elif self.adversaire.type == "terre":
            self.background = pygame.image.load("pokemon_game/images/BG-Plante.png")
            self.background = pygame.transform.scale(self.background, (800, 480))
        elif self.adversaire.type == "feu":
            self.background = pygame.image.load("pokemon_game/images/BG-Feu.png")
            self.background = pygame.transform.scale(self.background, (800, 480))
        elif self.adversaire.type == "normal":
            self.background = pygame.image.load("pokemon_game/images/BG-Normal.png")
            self.background = pygame.transform.scale(self.background, (800, 480))
    
    # définition de qui joue en premier entre le joueur et l'adversaire en fonction de l'initiative
    def definir_initiative(self):
        if random.randint(1, 20) + self.joueur.initiative > random.randint(1, 20) + self.adversaire.initiative:
            if self.joueur.pv > 0 and self.adversaire.pv > 0:
                self.tour_joueur()
            if self.joueur.pv > 0 and self.adversaire.pv > 0:
                self.tour_adversaire()
        else:
            if self.joueur.pv > 0 and self.adversaire.pv > 0:
                self.tour_adversaire()
            if self.joueur.pv > 0 and self.adversaire.pv > 0:
                self.tour_joueur()
    
    # méthode pour attaquer 
    def attaque(self, attaquant, defenseur):
        defenseur.pv -= attaquant.attaque * attaquant.comparaison(defenseur)
        text = f"{defenseur.nom} perd {attaquant.attaque * attaquant.comparaison(defenseur)} pv"
        text = self.police_texte.render(text, True, self.NOIR)
        self.fenetre.blit(text, (44, 402))
        pygame.display.flip()
        pygame.time.delay(2000)
        self.flip_fenetre()

    # définir si l'attaque touche ou rate en fonction de la défense de la cible
    def touche_attaque(self, attaquant, defenseur):
        if random.randint(1, 100) < 80-defenseur.defense:
            self.attaque(attaquant, defenseur)
        else:
            self.attaque_rate(attaquant)

    # affichage de l'attaque raté
    def attaque_rate(self, attaquant):
        text = f"{attaquant.nom} rate son attaque"
        text = self.police_texte.render(text, True, self.NOIR)
        self.fenetre.blit(text, (44, 402))
        pygame.display.flip()
        pygame.time.delay(2000)
        self.flip_fenetre()

    # affichage du gagnant du combat
    def affichage_gagnant(self, gagnant):
        self.gagnant = gagnant
        text = f"{gagnant} à gagné le match"
        text = self.police_texte.render(text, True, self.NOIR)
        self.fenetre.blit(text, (44, 402))
        pygame.display.flip()
        pygame.time.delay(2000)
        self.flip_fenetre()

    # méthode pour ajouter le pokémon battu au pokedex
    def ajout_pokedex(self):

        # chargement du fichier pokedex
        with open("pokemon_game/pokedex.json") as mon_fichier:
            data = json.load(mon_fichier)

        # verification des doublons
        if self.key_adversaire in data:
            data[self.key_adversaire] = data[self.key_adversaire] + 1
            with open("pokemon_game/pokedex.json", "w") as mon_fichier:
                json.dump(data, mon_fichier, indent=4)
        else:
            data[self.key_adversaire] = 1
            with open("pokemon_game/pokedex.json", "w") as mon_fichier:
                json.dump(data, mon_fichier, indent=4)

    # définition du tour du joueur
    def tour_joueur(self):

        # vérification si l'attaque touche
        self.touche_attaque(self.joueur, self.adversaire)

        # si le joueur gagne le combat:
        if self.adversaire.pv <= 0:
            self.ajout_pokedex()
            self.affichage_gagnant("Joueur")
            self.joueur.pv = self.joueur_pv_max
            self.joueur.gain_lvl()

            # si le pokemon evolue:
            if self.joueur.lvl == self.joueur.lvlEvolve:
                self.pokemon_joueur = self.joueur.evolution
                with open("pokemon_game/pokemon.json") as mon_fichier:
                    data = json.load(mon_fichier)
                dico_joueur = data[self.pokemon_joueur]
                self.sprite_joueur = pygame.image.load(dico_joueur["dos"])
                self.sprite_joueur = pygame.transform.scale(self.sprite_joueur, (160, 160))
                
                self.joueur.evol()
                self.texte_nom_joueur = self.police_texte.render(self.joueur.nom.upper(), True, self.NOIR)


    # definition du tour de l'adversaire
    def tour_adversaire(self):
        self.touche_attaque(self.adversaire, self.joueur)
        if self.joueur.pv <= 0:
            self.affichage_gagnant("L'adversaire")
            self.perdu = "menu"

    # mise a jour de l'affichage de la fenêtre
    def flip_fenetre(self):
        self.niveau_joueur = self.police_texte.render(str(self.joueur.lvl), True, self.NOIR)
        self.fenetre.blit(self.background, (0,0))
        self.fenetre.blit(self.sprite_joueur, (128,228))
        self.fenetre.blit(self.sprite_adversaire, (572,88))
        self.fenetre.blit(self.barre_joueur, (470,292))
        self.fenetre.blit(self.barre_ennemi, (48,72))
        self.fenetre.blit(self.texte_nom_joueur, (492, 304))
        self.fenetre.blit(self.niveau_joueur, (686, 304))
        self.fenetre.blit(self.texte_nom_adversaire, (70, 86))
        self.fenetre.blit(self.niveau_adversaire, (262, 88))

        # barre de vie du joueur
        pourcentage_joueur = (self.joueur.pv/self.joueur_pv_max) if self.joueur.pv > 0 else 0
        self.longueur_vie_joueur = int(160 * pourcentage_joueur)

        pygame.draw.rect(self.fenetre, self.VERT, (560, 331, self.longueur_vie_joueur, 8))

        # barre de vie de l'adversaire
        pourcentage_adversaire = (self.adversaire.pv/self.adversaire_pv_max) if self.adversaire.pv > 0 else 0
        self.longueur_vie_adversaire = int(160 * pourcentage_adversaire)

        pygame.draw.rect(self.fenetre, self.VERT, (130, 116, self.longueur_vie_adversaire, 8))

    # boucle d'évènements
    def gestion_evenement(self, evenements):
        for event in evenements:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.option_selectionnee = (self.option_selectionnee + 1) % len(self.options)
                elif event.key == pygame.K_UP:
                    self.option_selectionnee = (self.option_selectionnee - 1) % len(self.options)
                elif event.key == pygame.K_RETURN:
                    if self.gagnant == "Joueur":
                        if self.options[self.option_selectionnee] == "Oui":
                            self.gagnant = None
                            self.choix_adversaire()
                        elif self.options[self.option_selectionnee] == "Non":
                            return "menu"
                    else:
                        if self.options[self.option_selectionnee] == "Oui":
                            self.gagnant = None
                            self.joueur.pv = self.joueur_pv_max
                            self.choix_adversaire()
                        elif self.options[self.option_selectionnee] == "Non":
                            return "menu"
    # affichage du combat boucle de combat
    def afficher(self):
        pygame.display.set_caption("Combat Pokemon")
        self.flip_fenetre()
        while self.joueur.pv > 0 and self.adversaire.pv > 0:
            self.definir_initiative()

        # affichage du message de victoire
        if self.gagnant == "Joueur":
            text = "vous avez gagné! Commencer un nouveau match ?"
            text = self.police_texte.render(text, True, self.NOIR)
            self.fenetre.blit(text, (44, 402))
            self.fenetre.blit(self.ouiNon, (675, 392))
            for i, option in enumerate(self.options):
                texte_option = self.police_texte.render(option, True, self.NOIR)
                self.fenetre.blit(texte_option, (720, 405 + i * 30))
            self.fenetre.blit(self.fleche, (695, 405 + self.option_selectionnee * 30))
        # affichage du message de défaite
        else:
            text = "vous avez perdu. Retenter un match ?"
            text = self.police_texte.render(text, True, self.NOIR)
            self.fenetre.blit(text, (44, 402))
            self.fenetre.blit(self.ouiNon, (675, 392))
            for i, option in enumerate(self.options):
                texte_option = self.police_texte.render(option, True, self.NOIR)
                self.fenetre.blit(texte_option, (710, 405 + i * 30))
            self.fenetre.blit(self.fleche, (695, 405 + self.option_selectionnee * 30))