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
        self.barre_ennemi = pygame.image.load("pokemon_game/images/Barre-ennemi.png")
        self.barre_ennemi = pygame.transform.scale(self.barre_ennemi, (282, 78))
        self.barre_joueur = pygame.image.load("pokemon_game/images/Barre-joueur.png")
        self.barre_joueur = pygame.transform.scale(self.barre_joueur, (282, 78))
        self.police_texte = pygame.font.Font("pokemon_game/typographie/BOMBARD_.ttf", 20)
        self.texte_nom_adversaire = None
        self.niveau_adversaire = None

        with open("pokemon_game/pokemon.json") as mon_fichier:
            data = json.load(mon_fichier)
        dico_joueur = data[self.pokemon_joueur]
        self.joueur = pokemon(dico_joueur["nom"], dico_joueur["pv"], dico_joueur["initiative"],dico_joueur["lvlEvolve"], dico_joueur["evolution"], dico_joueur["type"], dico_joueur["attaque"], dico_joueur["defense"])
        self.sprite_joueur = pygame.image.load(dico_joueur["dos"])
        self.sprite_joueur = pygame.transform.scale(self.sprite_joueur, (160, 160))

        self.texte_nom_joueur = self.police_texte.render(self.joueur.nom.upper(), True, self.NOIR)
        self.choix_adversaire()

    def choix_adversaire(self):
        with open("pokemon_game/pokemon.json") as mon_fichier:
            data = json.load(mon_fichier)
        self.key_adversaire = random.choice(list(data.keys()))
        dico_adv = data[self.key_adversaire]
        self.adversaire = pokemon(dico_adv["nom"], dico_adv["pv"], dico_adv["initiative"],dico_adv["lvlEvolve"], dico_adv["evolution"], dico_adv["type"], dico_adv["attaque"], dico_adv["defense"])
        self.sprite_adversaire = pygame.image.load(dico_adv["face"])
        self.sprite_adversaire = pygame.transform.scale(self.sprite_adversaire, (160, 160))
        self.texte_nom_adversaire = self.police_texte.render(self.adversaire.nom.upper(), True, self.NOIR)
        self.niveau_adversaire = self.police_texte.render(str(self.adversaire.lvl), True, self.NOIR)

        level = 0
        if self.joueur.lvl == 1 or self.joueur.lvl == 2:
            level = random.randint(1, self.joueur.lvl + 2)
        else:
            level = random.randint(self.joueur.lvl - 2, self.joueur.lvl + 2)
        i = 0
        while i < level:
            self.adversaire.gain_lvl()
            i += 1

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
    
    def attaque(self, attaquant, defenseur):
        defenseur.pv -= attaquant.attaque * attaquant.comparaison(defenseur)
        text = f"{defenseur.nom} perd {attaquant.attaque * attaquant.comparaison(defenseur)} pv"
        text = self.police_texte.render(text, True, self.NOIR)
        self.fenetre.blit(text, (44, 402))
        pygame.display.flip()
        pygame.time.delay(2000)
        self.flip_fenetre()

    def touche_attaque(self, attaquant, defenseur):
        if random.randint(1, 100) < 80-defenseur.defense:
            self.attaque(attaquant, defenseur)
        else:
            self.attaque_rate(attaquant)

    def attaque_rate(self, attaquant):
        text = f"{attaquant.nom} rate son attaque"
        text = self.police_texte.render(text, True, self.NOIR)
        self.fenetre.blit(text, (44, 402))
        pygame.display.flip()
        pygame.time.delay(2000)
        self.flip_fenetre()

    def affichage_gagnant(self, gagnant):
        text = f"{gagnant} à gagné le match"
        text = self.police_texte.render(text, True, self.NOIR)
        self.fenetre.blit(text, (44, 402))
        pygame.display.flip()
        pygame.time.delay(2000)
        self.flip_fenetre()


    def ajout_pokedex(self):
        with open("pokemon_game/pokedex.json") as mon_fichier:
            data = json.load(mon_fichier)
        if self.key_adversaire in data:
            data[self.key_adversaire] = data[self.key_adversaire] + 1
            with open("pokemon_game/pokedex.json", "w") as mon_fichier:
                json.dump(data, mon_fichier, indent=4)
        else:
            data[self.key_adversaire] = 1
            with open("pokemon_game/pokedex.json", "w") as mon_fichier:
                json.dump(data, mon_fichier, indent=4)

    def tour_joueur(self):
        self.touche_attaque(self.joueur, self.adversaire)
        if self.adversaire.pv <= 0:
            self.affichage_gagnant(self.joueur.nom)
            self.joueur.gain_lvl()
    
    def tour_adversaire(self):
        self.touche_attaque(self.adversaire, self.joueur)
        if self.joueur.pv <= 0:
            self.affichage_gagnant(self.adversaire.nom)
            self.perdu = "menu"

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

    def gestion_evenement(self, evenements):
        pass

    def afficher(self):
        pygame.display.set_caption("Combat Pokemon")
        self.flip_fenetre()
        while self.joueur.pv > 0 and self.adversaire.pv > 0:
            self.definir_initiative()