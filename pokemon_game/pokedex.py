import pygame
import json
import sys

class pokedex():
    def __init__(self, fenetre):
        self.fenetre = fenetre

        # chargement des assets
        self.image_fond = pygame.image.load("pokemon_game/images/BG-dex.png")
        self.image_fond = pygame.transform.scale(self.image_fond, (800, 480))
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
        self.echap = self.police_texte.render("echap: retour", True, self.NOIR)

        # definition de la liste des pokemon
        self.liste_pokemon = []
        self.pokemon_selectionnee = 0
        self.liste_visible = 4
        with open("pokemon_game/pokemon.json") as mon_fichier:
            self.data = json.load(mon_fichier)
        for cle in self.data.keys():
            self.liste_pokemon.append(cle)

    # boucle d'évènements
    def gestion_evenement(self, evenements):
            for event in evenements:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self.pokemon_selectionnee = (self.pokemon_selectionnee + 1) % len(self.liste_pokemon)
                    elif event.key == pygame.K_UP:
                        self.pokemon_selectionnee = (self.pokemon_selectionnee - 1) % len(self.liste_pokemon)
                    elif event.key == pygame.K_ESCAPE:
                        return "menu"

    # affichage du pokedex en fonction du fichier pokedex.json
    def afficher(self):
        pygame.display.set_caption("Pokédex")
        self.fenetre.blit(self.image_fond, (0,0))
        self.fenetre.blit(self.bouton_selection, (508, 60))
        self.fenetre.blit(self.echap, (600, 10))

        # liste des pokemon a afficher dans le pokedex
        liste_pokedex =[]
        with open("pokemon_game/pokedex.json") as mon_fichier:
            data = json.load(mon_fichier)
        for cle in data.keys():
            liste_pokedex.append(cle)

        # affichage des boutons et des nom
        for i in range(0, 3):
            self.fenetre.blit(self.bouton_normal, (508, 156 + i*96))
        for i in range(self.liste_visible):
            index_pkm = (self.pokemon_selectionnee + i) % len(self.liste_pokemon)

            # si pokemon est dans le pokedex :
            if self.liste_pokemon[index_pkm] in liste_pokedex:
                dico_pokemon = self.data[self.liste_pokemon[index_pkm]]
                texte_pkm = self.police_texte.render((self.liste_pokemon[index_pkm]).upper(), True, self.NOIR)
                icon = pygame.image.load(dico_pokemon["miniature"])
                self.fenetre.blit(icon, (525, 80 + i * 96))
                self.fenetre.blit(texte_pkm, (576, 80 + i * 96))
                self.fenetre.blit(texte_pkm, (576, 80 + i * 96))
            # si pokemon n'est pas dans le pokedex:
            else:
                texte_pkm = self.police_texte.render(("????"), True, self.NOIR)
                self.fenetre.blit(texte_pkm, (576, 80 + i * 96))

        # affichage des stat si le pokemon est dans le pokedex
        if self.liste_pokemon[self.pokemon_selectionnee] in liste_pokedex:
            self.affichage_stat()
            nbr_pkm = self.police_texte.render(str(data[self.liste_pokemon[self.pokemon_selectionnee]]), True, self.NOIR)
            self.fenetre.blit(nbr_pkm, (350, 425))
        # affichage masqué si le pokemon n'est pas dans la pokedex
        else:
            self.affichage_masque()
    
    # affichages des stat
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

    # affichage masqué
    def affichage_masque(self):
        texte_nom = self.police_texte.render("????", True, self.NOIR)
        texte_stat = self.police_texte.render("??", True, self.NOIR)

        self.fenetre.blit(self.sprite_inconnu, (95, 125))
        self.fenetre.blit(texte_nom, (268, 106))
        self.fenetre.blit(texte_stat, (160, 304))
        self.fenetre.blit(texte_stat, (160, 359))
        self.fenetre.blit(texte_stat, (388, 304))
        self.fenetre.blit(texte_stat, (388, 359))