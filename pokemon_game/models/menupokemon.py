import pygame
import sys
import json
class menuPokemon:
    def __init__(self, fond, largeur_fenetre, hauteur_fenetre, fenetre):
        self.NOIR = (0, 0, 0)
        self.fenetre = fenetre
        self.image_fond = fond
        self.image_fond = pygame.transform.scale(self.image_fond, (largeur_fenetre, hauteur_fenetre))
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
        self.police_texte = pygame.font.Font("pokemon_game/typographie/BOMBARD_.ttf", 30)
        self.liste_pokemon = []
        self.pokemon_selectionnee = 0
        self.liste_visible = 4
        with open("pokemon_game/pokemon.json") as mon_fichier:
            self.data = json.load(mon_fichier)
        for cle in self.data.keys():
            self.liste_pokemon.append(cle)

    def selection(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self.pokemon_selectionnee = (self.pokemon_selectionnee + 1) % len(self.liste_pokemon)
                    elif event.key == pygame.K_UP:
                        self.pokemon_selectionnee = (self.pokemon_selectionnee - 1) % len(self.liste_pokemon)
                    elif event.key == pygame.K_RETURN:
                        pokemon_joueur = self.liste_pokemon[self.pokemon_selectionnee]
                        from combat import combat
                        combat.py
            self.affichage_game()

    def pokedex(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self.pokemon_selectionnee = (self.pokemon_selectionnee + 1) % len(self.liste_pokemon)
                    elif event.key == pygame.K_UP:
                        self.pokemon_selectionnee = (self.pokemon_selectionnee - 1) % len(self.liste_pokemon)
                    elif event.key == pygame.K_RETURN:
                        import menu
                        menu.py
                    elif event.key == pygame.K_ESCAPE:
                        import menu
                        menu.py
            self.affichage_pokedex()

    def affichage_game(self):
        self.fenetre.blit(self.image_fond, (0,0))
        self.fenetre.blit(self.bouton_selection, (508, 60))
        for i in range(0, 3):
            self.fenetre.blit(self.bouton_normal, (508, 156 + i*96))
        for i in range(self.liste_visible):
            index_pkm = (self.pokemon_selectionnee + i) % len(self.liste_pokemon)
            texte_pkm = self.police_texte.render((self.liste_pokemon[index_pkm]).upper(), True, self.NOIR)
            self.fenetre.blit(texte_pkm, (576, 80 + i * 96))
        self.affichage_stat()

    def affichage_pokedex(self):
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
                texte_pkm = self.police_texte.render((self.liste_pokemon[index_pkm]).upper(), True, self.NOIR)
                self.fenetre.blit(texte_pkm, (576, 80 + i * 96))
            else:
                texte_pkm = self.police_texte.render(("????"), True, self.NOIR)
                self.fenetre.blit(texte_pkm, (576, 80 + i * 96))
        if self.liste_pokemon[self.pokemon_selectionnee] in liste_pokedex:
            self.affichage_stat()
        else:
            self.affichage_masque()
    
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

        self.fenetre.blit(texte_nom, (268, 106))
        self.fenetre.blit(texte_pv, (160, 304))
        self.fenetre.blit(texte_atk, (160, 359))
        self.fenetre.blit(texte_vit, (388, 304))
        self.fenetre.blit(texte_def, (388, 359))
        
        pygame.display.flip()

    def affichage_masque(self):
        dico_pokemon = self.data[self.liste_pokemon[self.pokemon_selectionnee]]
        texte_nom = self.police_texte.render("????", True, self.NOIR)
        texte_pv = self.police_texte.render("??", True, self.NOIR)
        texte_atk = self.police_texte.render("??", True, self.NOIR)
        texte_vit = self.police_texte.render("??", True, self.NOIR)
        texte_def = self.police_texte.render("??", True, self.NOIR)

        self.fenetre.blit(texte_nom, (268, 106))
        self.fenetre.blit(texte_pv, (160, 304))
        self.fenetre.blit(texte_atk, (160, 359))
        self.fenetre.blit(texte_vit, (388, 304))
        self.fenetre.blit(texte_def, (388, 359))
        
        pygame.display.flip()