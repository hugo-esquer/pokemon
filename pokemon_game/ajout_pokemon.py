import json
import pygame

class Button:

    def __init__(self, x, y, width, height, image_path, action):
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.action = action

    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.action()

class PokemonApp:

    def __init__(self, largeur_fenetre, hauteur_fenetre, image_fond_path):
        pygame.init()

        # Paramètres de la fenêtre
        self.largeur_fenetre = largeur_fenetre
        self.hauteur_fenetre = hauteur_fenetre

        # Image de fond
        self.image_fond = pygame.image.load(image_fond_path)
        self.image_fond = pygame.transform.scale(self.image_fond, (self.largeur_fenetre, self.hauteur_fenetre))

        # Création de la fenêtre
        self.fenetre = pygame.display.set_mode((self.largeur_fenetre, self.hauteur_fenetre))
        pygame.display.set_caption("Pokemon")

        # Liste de boutons
        self.buttons = [
            Button(50, 220, 140, 40, "pokemon_game/images/Type-eau.png", self.button1_action),
            Button(225, 220, 140, 40, "pokemon_game/images/Type-feu.png", self.button2_action),
            Button(100, 330, 140, 40, "pokemon_game/images/ajout.pokemon.FORT.png", self.button3_action),
            Button(500, 330, 140, 40, "pokemon_game/images/ajout.pokemon.FAIBLE.png", self.button4_action),
            Button(410, 220, 140, 40, "pokemon_game/images/Type-normal.png", self.button5_action),
            Button(300, 330, 140, 40, "pokemon_game/images/ajout.pokemon.MOYEN.png", self.button6_action),
            Button(600, 220, 140, 40, "pokemon_game/images/Type-plante.png", self.button7_action),
            Button(300, 420, 140, 40, "pokemon_game\images\VALIDER.png", self.button8_action),
        ]

    def button1_action(self):
        print("Action du Bouton 1")

    def button2_action(self):
        print("Action du Bouton 2")

    def button3_action(self):
        print("Action du Bouton 3")

    def button4_action(self):
        print("Action du Bouton 4")

    def button5_action(self):
        print("Action du Bouton 5")

    def button6_action(self):
        print("Action du Bouton 6")

    def button7_action(self):
        print("Action du Bouton 7")

    def button8_action(self):
        print("Action du bouton 8")

    def run(self):
        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return  # Sort de la boucle infinie et termine le programme

                # Gère les événements des boutons
                for button in self.buttons:
                    button.handle_event(event)

            self.fenetre.blit(self.image_fond, (0, 0))

            # Dessine les boutons
            for button in self.buttons:
                button.draw(self.fenetre)

            pygame.display.flip()
            clock.tick(60)  # Limite la boucle à 60 images par seconde


if __name__ == "__main__":
    app = PokemonApp(800, 480, "pokemon_game/images/background.ajout.png")
    app.run()
