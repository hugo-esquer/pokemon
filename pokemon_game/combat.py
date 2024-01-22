import random
import json
import pygame
from models.pokemon import pokemon


class combat():
    def __init__(self, fenetre, joueur):
        self.fenetre = fenetre
        self.joueur = joueur
        self.adversaire = None
        self.key_adversaire = None
        self.background = None

        with open("pokemon_game/pokemon.json") as mon_fichier:
            data = json.load(mon_fichier)
        self.key_adversaire = random.choice(list(data.keys()))
        dico_adv = data[self.key_adversaire]
        self.adversaire = pokemon(dico_adv["nom"], dico_adv["pv"], dico_adv["initiative"],dico_adv["lvlEvolve"], dico_adv["evolution"], dico_adv["type"], dico_adv["attaque"], dico_adv["defense"])

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
            self.tour_joueur()
            self.tour_adversaire()
        else:
            self.tour_adversaire()
            self.tour_joueur()
    
    def attaque(self, attaquant, defenseur):
        defenseur.pv -= attaquant.attaque * attaquant.comparaison(defenseur)
        text = f"{defenseur.nom} perd {attaquant.attaque * attaquant.comparaison(defenseur)} pv"
        text = self.police_texte.render(text)
        self.fenetre.blit(text, (44, 402))

    def touche_attaque(self, attaquant, defenseur):
        if random.randint(1, 100) < 80-defenseur.defense:
            self.attaque(attaquant, defenseur)
        else:
            self.attaque_rate(attaquant)

    def attaque_rate(self, attaquant):
        text = f"{attaquant.nom} rate son attaque"
        text = self.police_texte.render(text)
        self.fenetre.blit(text, (44, 402))

    def affichage_gagnant(self, gagnant):
        text = f"{gagnant} à gagné le match"
        text = self.police_texte.render(text)
        self.fenetre.blit(text, (44, 402))


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
    
    def tour_adversaire(self):
        self.touche_attaque(self.adversaire, self.joueur)
        if self.joueur.pv <= 0:
            self.affichage_gagnant(self.adversaire.nom)

    def gestion_evenement(self, evenements):
        pass

    def afficher(self):
        pygame.display.set_caption("Combat Pokemon")
        self.fenetre.blit(self.background, (0,0))