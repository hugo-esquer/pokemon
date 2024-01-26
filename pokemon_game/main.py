import pygame
import sys

class PokemonGame:
    def __init__(self):
        pygame.init()
        self.largeur_fenetre = 800
        self.hauteur_fenetre = 480
        self.fenetre = pygame.display.set_mode((self.largeur_fenetre, self.hauteur_fenetre))
        pygame.display.set_caption("Pokemon")

        self.image_fond = pygame.image.load("pokemon_game\\images\\background.accueil.jpg")
        self.image_fond = pygame.transform.scale(self.image_fond, (self.largeur_fenetre, self.hauteur_fenetre))

        self.couleur_bouton_normal = (255, 165, 0)
        self.couleur_bouton_survol = (255, 200, 0)
        self.couleur_bouton_clic = (255, 100, 0)
        self.couleur_texte = (0, 0, 0)

        self.largeur_bouton = 300
        self.hauteur_bouton = 50

        self.x_bouton = (self.largeur_fenetre - self.largeur_bouton) // 2
        self.y_bouton1 = (self.hauteur_fenetre - (self.hauteur_bouton * 2 + 10)) // 2
        self.y_bouton2 = self.y_bouton1 + self.hauteur_bouton + 60

        self.couleur_bouton1 = self.couleur_bouton_normal
        self.couleur_bouton2 = self.couleur_bouton_normal

    def dessiner_bouton(self, x, y, largeur, hauteur, texte, couleur):
        pygame.draw.rect(self.fenetre, couleur, (x, y, largeur, hauteur))
        font = pygame.font.SysFont('Bombardier', 24)
        texte_surface = font.render(texte, True, self.couleur_texte)
        texte_rect = texte_surface.get_rect(center=(x + largeur // 2, y + hauteur // 2))
        self.fenetre.blit(texte_surface, texte_rect)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEMOTION:
                    x, y = event.pos
                    if self.x_bouton < x < self.x_bouton + self.largeur_bouton and self.y_bouton1 < y < self.y_bouton1 + self.hauteur_bouton:
                        self.couleur_bouton1 = self.couleur_bouton_survol
                    else:
                        self.couleur_bouton1 = self.couleur_bouton_normal

                    if self.x_bouton < x < self.x_bouton + self.largeur_bouton and self.y_bouton2 < y < self.y_bouton2 + self.hauteur_bouton:
                        self.couleur_bouton2 = self.couleur_bouton_survol
                    else:
                        self.couleur_bouton2 = self.couleur_bouton_normal

                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if self.x_bouton < x < self.x_bouton + self.largeur_bouton and self.y_bouton1 < y < self.y_bouton1 + self.hauteur_bouton:
                        self.couleur_bouton1 = self.couleur_bouton_clic
                        return "menu"

                    if self.x_bouton < x < self.x_bouton + self.largeur_bouton and self.y_bouton2 < y < self.y_bouton2 + self.hauteur_bouton:
                        self.couleur_bouton2 = self.couleur_bouton_clic
                        pygame.quit()
                        sys.exit()

            self.fenetre.blit(self.image_fond, (0, 0))

            self.dessiner_bouton(self.x_bouton, self.y_bouton1, self.largeur_bouton, self.hauteur_bouton, "ACCUEIL", self.couleur_bouton1)
            self.dessiner_bouton(self.x_bouton, self.y_bouton2, self.largeur_bouton, self.hauteur_bouton, "QUITTER", self.couleur_bouton2)

            pygame.display.flip()

if __name__ == "__main__":
    jeu = PokemonGame()
    jeu.run()
