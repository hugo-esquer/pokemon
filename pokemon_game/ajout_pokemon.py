import json
import pygame
import sys

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

    def draw(self, surface):
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        surface.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))

class PokemonApp:

    def __init__(self, largeur_fenetre, hauteur_fenetre, image_fond_path):
        pygame.init()
        self.largeur_fenetre = largeur_fenetre
        self.hauteur_fenetre = hauteur_fenetre
        self.image_fond = pygame.image.load(image_fond_path)
        self.image_fond = pygame.transform.scale(self.image_fond, (self.largeur_fenetre, self.hauteur_fenetre))
        self.fenetre = pygame.display.set_mode((self.largeur_fenetre, self.hauteur_fenetre))
        pygame.display.set_caption("Ajouter un pokemon")

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

    def button1_action(self):
        print(f"Action du Bouton 1 - Type : {self.type_buttons[0].type}")

    def button2_action(self):
        print(f"Action du Bouton 2 - Type : {self.type_buttons[1].type}")

    def button3_action(self):
        print(f"Action du Bouton 3 - Force : {self.other_buttons[0].force}")

    def button4_action(self):
        print(f"Action du Bouton 4 - Force : {self.other_buttons[1].force}")

    def button5_action(self):
        print(f"Action du Bouton 5 - Type : {self.type_buttons[2].type}")

    def button6_action(self):
        print(f"Action du Bouton 6 - Force : {self.other_buttons[2].force}")

    def button7_action(self):
        print(f"Action du Bouton 7 - Type : {self.type_buttons[3].type}")

    def button8_action(self):
        print("Action du bouton 8")

    def run(self):
        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                for button in self.type_buttons + self.other_buttons + self.ajouter_buttons:
                    button.handle_event(event)

                self.text_input.handle_event(event)

            for button in self.type_buttons + self.other_buttons + self.ajouter_buttons:
                button.update()

            self.fenetre.blit(self.image_fond, (0, 0))

            for button in self.type_buttons + self.other_buttons + self.ajouter_buttons:
                button.draw(self.fenetre)

            self.text_input.draw(self.fenetre)

            pygame.display.flip()
            clock.tick(60)

if __name__ == "__main__":
    app = PokemonApp(800, 480, "pokemon_game/images/background.ajout.png")
    pygame.event.set_grab(False)
    app.run()



# une variable type 
# une variable type selectionné tant que type selectionné = none tu peux cliquer 
# type selectionné = none 
# if type selectionne == none 
# faire une focntion faible qui prend  qui créer un dictionnaire 

# def faible (type, nom):

#   with open("pokemon_game/pokedex.json") as mon_fichier:
#             data = json.load(mon_fichier)
#             data [hericendre = nom ]

#     with open("pokemon_game/pokedex.json", "w") as mon_fichier:
#     json.dump(data, mon_fichier, indent=4)

#                 # sort_keys pour aller a la ligne 