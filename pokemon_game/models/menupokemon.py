import pygame
import sys
import json

class menuPokemon:
    def __init__(self):
        self.NOIR = (0, 0, 0)
        self.bouton_normal = pygame.image.load("pokemon_game/images/Bouton-nonselection.png")
        self.bouton_normal = pygame.transform.scale(self.bouton_normal, (264, 72))
        self.bouton_selection = pygame.image.load("pokemon_game/images/Bouton-selection.png")
        self.bouton_selection = pygame.transform.scale(self.bouton_selection, (264, 72))
        self.type_eau = pygame.image.load("pokemon_game/images/Type-eau.png")
        self.type_eau = pygame.transform.scale(self.type_eau, (196, 36))
        self.type_feu = pygame.image.load("pokemon_game/images/Type-feu.png")
        self.type_feu = pygame.transform.scale(self.type_feu, (196, 36))
        self.type_plante = pygame.image.load("pokemon_game/images/Type-plante.png")
        self.type_plante = pygame.transform.scale(self.type_plante, (196, 36))
        self.type_normal = pygame.image.load("pokemon_game/images/Type-normal.png")
        self.type_normal = pygame.transform.scale(self.type_normal, (196, 36))
        self.sprite_inconnu = pygame.image.load("pokemon_game/images/Sprite-inconnu.png")
        self.sprite_inconnu = pygame.transform.scale(self.sprite_inconnu, (128, 128))
        self.police_texte = pygame.font.Font("pokemon_game/typographie/BOMBARD_.ttf", 30)
        self.liste_pokemon = []
        self.pokemon_selectionnee = 0
        self.liste_visible = 4
        with open("pokemon_game/pokemon.json") as mon_fichier:
            self.data = json.load(mon_fichier)
        for cle in self.data.keys():
            self.liste_pokemon.append(cle)

    def affichage_stat(self):
        dico_pokemon = self.data[self.liste_pokemon[self.pokemon_selectionnee]]
        texte_nom = self.police_texte.render(dico_pokemon["nom"], True, self.NOIR)
        texte_pv = self.police_texte.render(str(dico_pokemon["pv"]), True, self.NOIR)
        texte_atk = self.police_texte.render(str(dico_pokemon["attaque"]), True, self.NOIR)
        texte_vit = self.police_texte.render(str(dico_pokemon["initiative"]), True, self.NOIR)
        texte_def = self.police_texte.render(str(dico_pokemon["defense"]), True, self.NOIR)
        if dico_pokemon["type"] == "eau":
            self.fenetre.blit(self.type_eau, (260, 152))
        if dico_pokemon["type"] == "feu":
            self.fenetre.blit(self.type_feu, (260, 152))
        if dico_pokemon["type"] == "terre":
            self.fenetre.blit(self.type_plante, (260, 152))
        if dico_pokemon["type"] == "normal":
            self.fenetre.blit(self.type_normal, (260, 152))
        sprite_pokemon = pygame.image.load(dico_pokemon["face"])
        sprite_pokemon = pygame.transform.scale(sprite_pokemon, (160, 160))

        self.fenetre.blit(sprite_pokemon, (80, 112))
        self.fenetre.blit(texte_nom, (268, 106))
        self.fenetre.blit(texte_pv, (160, 304))
        self.fenetre.blit(texte_atk, (160, 359))
        self.fenetre.blit(texte_vit, (388, 304))
        self.fenetre.blit(texte_def, (388, 359))

    def affichage_masque(self):
        texte_nom = self.police_texte.render("????", True, self.NOIR)
        texte_pv = self.police_texte.render("??", True, self.NOIR)
        texte_atk = self.police_texte.render("??", True, self.NOIR)
        texte_vit = self.police_texte.render("??", True, self.NOIR)
        texte_def = self.police_texte.render("??", True, self.NOIR)

        self.fenetre.blit(self.sprite_inconnu, (95, 125))
        self.fenetre.blit(texte_nom, (268, 106))
        self.fenetre.blit(texte_pv, (160, 304))
        self.fenetre.blit(texte_atk, (160, 359))
        self.fenetre.blit(texte_vit, (388, 304))
        self.fenetre.blit(texte_def, (388, 359))