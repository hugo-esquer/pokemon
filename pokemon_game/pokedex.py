import pygame
import json
import sys
from models.menupokemon import menuPokemon


class pokedex(menuPokemon):
    def __init__(self, fenetre):
        self.fenetre = fenetre
        self.image_fond = pygame.image.load("pokemon_game/images/BG-dex.png")
        self.image_fond = pygame.transform.scale(self.image_fond, (800, 480))

    def gestion_evenement(self, evenements):
        while True:
            for event in evenements:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self.pokemon_selectionnee = (self.pokemon_selectionnee + 1) % len(self.liste_pokemon)
                    elif event.key == pygame.K_UP:
                        self.pokemon_selectionnee = (self.pokemon_selectionnee - 1) % len(self.liste_pokemon)
                    elif event.key == pygame.K_RETURN:
                        return "menu"
                    elif event.key == pygame.K_ESCAPE:
                        return "menu"


    def afficher(self):
        pygame.display.set_caption("Pokédex")
        self.fenetre.blit(self.image_fond, (0,0))
        self.fenetre.blit(self.bouton_selection, (508, 60))
        liste_pokedex =[]
        with open("pokemon_game/pokedex.json") as mon_fichier:
            data = json.load(mon_fichier)
        for cle in data.keys():
            liste_pokedex.append(cle)
        for i in range(0, 3):
            self.fenetre.blit(self.bouton_normal, (508, 156 + i*96))
        for i in range(self.liste_visible):
            index_pkm = (self.pokemon_selectionnee + i) % len(self.liste_pokemon)
            if self.liste_pokemon[index_pkm] in liste_pokedex:
                dico_pokemon = self.data[self.liste_pokemon[index_pkm]]
                texte_pkm = self.police_texte.render((self.liste_pokemon[index_pkm]).upper(), True, self.NOIR)
                icon = pygame.image.load(dico_pokemon["miniature"])
                self.fenetre.blit(icon, (525, 80 + i * 96))
                self.fenetre.blit(texte_pkm, (576, 80 + i * 96))
                self.fenetre.blit(texte_pkm, (576, 80 + i * 96))
            else:
                texte_pkm = self.police_texte.render(("????"), True, self.NOIR)
                self.fenetre.blit(texte_pkm, (576, 80 + i * 96))
        if self.liste_pokemon[self.pokemon_selectionnee] in liste_pokedex:
            self.affichage_stat()
            nbr_pkm = self.police_texte.render(str(data[self.liste_pokemon[self.pokemon_selectionnee]]), True, self.NOIR)
            self.fenetre.blit(nbr_pkm, (350, 425))
            pygame.display.flip()
        else:
            self.affichage_masque()
