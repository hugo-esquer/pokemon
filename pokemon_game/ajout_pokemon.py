import json
import pygame
import sys
import random

class Button:

    def __init__(self, x, y, width, height, image_path, action, button_type=None, button_force=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.image_original = pygame.image.load(image_path)
        self.image_original = pygame.transform.scale(self.image_original, (width, height))
        self.image = self.image_original.copy()
        self.action = action
        self.clicked = False
        self.type = button_type  # Ajout de la variable de type
        self.force = button_force  # Ajout de la variable de force

    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.clicked = not self.clicked
                self.action()

    def update(self):
        if self.clicked:
            self.image = pygame.transform.scale(self.image_original, (int(self.rect.width * 0.9), int(self.rect.height * 0.9)))
        else:
            self.image = self.image_original.copy()

class TextInput:

    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = ""
        self.font = pygame.font.SysFont("Bombardier", 32)
        self.active = False

        #récupérer la valeur entrée et l'ajoute au fichier json

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.active = self.rect.collidepoint(event.pos)
        elif event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_RETURN:
                self.active = False
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode

    def get_text (self):
        return self.text.lower()

    def draw(self, surface):
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        surface.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))

class PokemonApp:

    def __init__(self, fenetre):
        pygame.init()
        self.largeur_fenetre = 800
        self.hauteur_fenetre = 480
        self.image_fond = pygame.image.load("pokemon_game/images/background.ajout.png")
        self.image_fond = pygame.transform.scale(self.image_fond, (self.largeur_fenetre, self.hauteur_fenetre))
        self.fenetre = fenetre
        self.type_selectionne= None
        self.force_selectionne = None
        self.cle = None
        self.dico={}
        self.police_texte = pygame.font.Font("pokemon_game/typographie/BOMBARD_.ttf", 30)
        self.echap = self.police_texte.render("echap: retour", True, (0, 0, 0))

        self.type_buttons = [
            Button(50, 220, 140, 40, "pokemon_game/images/Type-eau.png", self.button1_action, button_type="Eau"),
            Button(225, 220, 140, 40, "pokemon_game/images/Type-feu.png", self.button2_action, button_type="Feu"),
            Button(410, 220, 140, 40, "pokemon_game/images/Type-normal.png", self.button5_action, button_type="Normal"),
            Button(600, 220, 140, 40, "pokemon_game/images/Type-plante.png", self.button7_action, button_type="Plante"),
        ]

        self.other_buttons = [
            Button(100, 330, 140, 40, "pokemon_game/images/ajout.pokemon.FORT.png", self.button3_action, button_force="fort"),
            Button(500, 330, 140, 40, "pokemon_game/images/ajout.pokemon.FAIBLE.png", self.button4_action, button_force="faible"),
            Button(300, 330, 140, 40, "pokemon_game/images/ajout.pokemon.MOYEN.png", self.button6_action, button_force="moyen"),
        ]

        self.ajouter_buttons = [
            Button(300, 420, 140, 40, "pokemon_game\images\VALIDER.png", self.button8_action)
        ]

        self.text_input = TextInput(190, 125, 410, 40)

    def faible(self):
        self.dico["nom"] = self.cle.capitalize()
        self.dico["type"]= self.type_selectionne
        self.dico["pv"]= random.randint(40, 50)
        self.dico["attaque"]= random.randint(20, 36)
        self.dico["defense"]= random.randint(5, 28)
        self.dico["initiative"]= random.randint(4,5)
        self.dico["lvlEvolve"]= None
        self.dico["evolution"]= None
        self.dico["face"]= "pokemon_game/images/Sprites/132-Front.png"
        self.dico["dos"]= "pokemon_game/images/Sprites/132-Back.png"
        self.dico["miniature"]= "pokemon_game/images/Sprites/132-Icon.png"
        
    def moyen(self):
        self.dico["nom"] = self.cle.capitalize()
        self.dico["type"]= self.type_selectionne
        self.dico["pv"]= random.randint(50, 60)
        self.dico["attaque"]= random.randint(36, 52)
        self.dico["defense"]= random.randint(28, 51)
        self.dico["initiative"]= random.randint(5,6)
        self.dico["lvlEvolve"]= None
        self.dico["evolution"]= None
        self.dico["face"]= "pokemon_game/images/Sprites/132-Front.png"
        self.dico["dos"]= "pokemon_game/images/Sprites/132-Back.png"
        self.dico["miniature"]= "pokemon_game/images/Sprites/132-Icon.png"

    def fort(self):
        self.dico["nom"] = self.cle.capitalize()
        self.dico["type"]= self.type_selectionne
        self.dico["pv"]= random.randint(60, 70)
        self.dico["attaque"]= random.randint(52, 68)
        self.dico["defense"]= random.randint(51, 75)
        self.dico["initiative"]= random.randint(6, 7)
        self.dico["lvlEvolve"]= None
        self.dico["evolution"]= None
        self.dico["face"]= "pokemon_game/images/Sprites/132-Front.png"
        self.dico["dos"]= "pokemon_game/images/Sprites/132-Back.png"
        self.dico["miniature"]= "pokemon_game/images/Sprites/132-Icon.png"

    def button1_action(self):
        print(f"Action du Bouton 1 - Type : {self.type_buttons[0].type}")
        self.type_selectionne = "eau"
        
    def button2_action(self):
        print(f"Action du Bouton 2 - Type : {self.type_buttons[1].type}")
        self.type_selectionne = "feu"

    def button3_action(self):
        print(f"Action du Bouton 3 - Force : {self.other_buttons[0].force}")
        self.force_selectionne = "fort"

    def button4_action(self):
        print(f"Action du Bouton 4 - Force : {self.other_buttons[1].force}")
        self.force_selectionne = "faible"

    def button5_action(self):
        print(f"Action du Bouton 5 - Type : {self.type_buttons[2].type}")
        self.type_selectionne = "normal"

    def button6_action(self):
        print(f"Action du Bouton 6 - Force : {self.other_buttons[2].force}")
        self.force_selectionne = "moyen"

    def button7_action(self):
        print(f"Action du Bouton 7 - Type : {self.type_buttons[3].type}")
        self.type_selectionne = "terre"

    def button8_action(self):
        self.cle = self.text_input.get_text()
        if self.type_selectionne == "plante":
            if self.force_selectionne == "faible":
                self.faible()
            if self.force_selectionne == "moyen":
                self.moyen()
            if self.force_selectionne == "fort":
                self.fort()
        elif self.type_selectionne == "normal":
            if self.force_selectionne == "faible":
                self.faible()
            if self.force_selectionne == "moyen":
                self.moyen()
            if self.force_selectionne == "fort":
                self.fort()
        elif self.type_selectionne == "feu":
            if self.force_selectionne == "faible":
                self.faible()
            if self.force_selectionne == "moyen":
                self.moyen()
            if self.force_selectionne == "fort":
                self.fort()
        elif self.type_selectionne == "eau":
            if self.force_selectionne == "faible":
                self.faible()
            if self.force_selectionne == "moyen":
                self.moyen()
            if self.force_selectionne == "fort":
                self.fort()

        with open("pokemon_game/pokemon.json") as mon_fichier:
            data = json.load(mon_fichier)

        data[f"{self.cle}"] = self.dico
        with open("pokemon_game/pokemon.json", "w") as mon_fichier:
            json.dump(data, mon_fichier, sort_keys=True, indent=4)

    def gestion_evenement(self, evenements):

        for event in evenements:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "menu"

            for button in self.type_buttons + self.other_buttons + self.ajouter_buttons:
                button.handle_event(event)

            self.text_input.handle_event(event)

        for button in self.type_buttons + self.other_buttons + self.ajouter_buttons:
            button.update()

    def afficher (self):
        pygame.display.set_caption("Ajouter un pokemon")
        clock = pygame.time.Clock()
        self.fenetre.blit(self.image_fond, (0, 0))
        self.fenetre.blit(self.echap, (600, 10))

        for button in self.type_buttons + self.other_buttons + self.ajouter_buttons:
            button.draw(self.fenetre)

        self.text_input.draw(self.fenetre)

        pygame.display.flip()
        clock.tick(60)