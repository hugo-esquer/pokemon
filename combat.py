import random, json, pokemon

class combat:
    def __init__(self, joueur):
        self.joueur = joueur
        self.adversaire = None

    def random_adv(self):
        with open("pokemon.json") as mon_fichier:
            data = json.load(mon_fichier)
        key_adversaire = random.choice(list(data.key()))
        dico_adv = data[key_adversaire]
        self.adversaire = pokemon(dico_adv["nom"], dico_adv["pv"], dico_adv["initiative"],dico_adv["lvlEvolve"], dico_adv["evolution"], dico_adv["type"], dico_adv["attaque"], dico_adv["defense"])

    def definir_lvl_adv(self):
        level = 0
        if self.joueur.lvl == 1 or self.joueur.lvl == 2:
            level = random.randint(1, self.joueur.lvl + 2)
        else:
            level = random.randint(self.joueur.lvl - 2, self.joueur.lvl + 2)
        while i < level:
            self.adversaire.gain_lvl()
            i += 1

    def definir_terrain(self):
        if self.adversaire.type == "eau":
            cercle = pygame.image.load(images/"cercle_eau.png")
            fond = pygame.image.load(images/"mer.png")
        elif self.adversaire.type == "terre":
            cercle = pygame.image.load(images/"cerlce_terre.png")
            fond = pygame.image.load(images/"foret.png")
        elif self.adversaire.type == "feu":
            cercle = pygame.image.load(images/"cercle_feu.png")
            fond = pygame.image.load(images/"boue.png")
        elif self.adversaire.type == "neutre":
            cercle = pygame.image.load(images/"cercle_neutre.png")
            fond = pygame.image.load(images/"plaine.png")
    
    def definir_initiative(self):
        if random.randint(1, 20) + self.joueur.initiative > random.randint(1, 20) + self.adversaire.initiative:
            self.tour_joueur()
            self.tour_adversaire()
        else:
            self.tour_adversaire()
            self.tour_joueur()
    
    def attaque(self, attaquant, defenseur):
        defenseur.pv -= attaquant.attaque * attaquant.comparaison(defenseur)
        print(f"{self.defenseur.nom} perd {attaquant.attaque * attaquant.comparaison(defenseur)} pv")
    
    def touche_attaque(self, attaquant, defenseur):
        if random.randint(1, 100) < 80-defenseur.defense:
            self.attaque(attaquant, defenseur)
        else:
            self.attaque_rate()

    def attaque_rate(self, attaquant):
        print(f"{attaquant.nom} rate son attaque")

    def affichage_gagnant(self, gagnant):
        pass

    def ajout_pokedex(self):
        with open("pokedex.json") as mon_fichier:
            data = json.load(mon_fichier)
        data[self.adversaire.nom] = {"nom": self.adversaire.nom, "type": self.adversaire.type, "PV": self.adversaire.pv, "attaque": self.adversaire.attaque, "defense": self.adversaire.defense, "initiative": self.adversaire.initiative}
        with open("pokedex.json") as mon_fichier:
            json.dump(data, mon_fichier)

    def tour_joueur(self):
        self.touche_attaque(self.joueur, self.adversaire)
        if self.adversaire.pv <= 0:
            self.affichage_gagnant(self.joueur.nom)
    
    def tour_adversaire(self):
        self.touche_attaque(self.adversaire, self.joueur)
        if self.joueur.pv <= 0:
            self.affichage_gagnant(self.adversaire.nom)
    

    
