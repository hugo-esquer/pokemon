import pygame
import sys

# Chargement et initialisation audio
mouse_over_button_sound = pygame.mixer.Sound("pokemon_game/audio/bruitages/mouse_over_button.mp3")
mouse_over_button_sound.set_volume(0.25)
launch_party_click_button_sound = pygame.mixer.Sound("pokemon_game/audio/bruitages/launch_party_click_button.mp3")
pygame.mixer.music.load("pokemon_game/audio/ambiances_musiques/opening_Theme.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.25)
play_sound1 = False
play_sound2 = False


class PokemonGame:
    def __init__(self,fenetre):
        pygame.init()
        self.fenetre = fenetre

        self.image_fond = pygame.image.load("pokemon_game\\images\\background.accueil.jpg")
        self.image_fond = pygame.transform.scale(self.image_fond, (800, 480))

        self.couleur_bouton_normal = (255, 165, 0)
        self.couleur_bouton_survol = (255, 200, 0)
        self.couleur_bouton_clic = (255, 100, 0)
        self.couleur_texte = (0, 0, 0)

        self.largeur_bouton = 300
        self.hauteur_bouton = 50

        self.x_bouton = (800 - self.largeur_bouton) // 2
        self.y_bouton1 = (480 - (self.hauteur_bouton * 2 + 10)) // 2
        self.y_bouton2 = self.y_bouton1 + self.hauteur_bouton + 60

        self.couleur_bouton1 = self.couleur_bouton_normal
        self.couleur_bouton2 = self.couleur_bouton_normal

    def dessiner_bouton(self, x, y, largeur, hauteur, texte, couleur):
        pygame.draw.rect(self.fenetre, couleur, (x, y, largeur, hauteur))
        font = pygame.font.SysFont('Bombardier', 24)
        texte_surface = font.render(texte, True, self.couleur_texte)
        texte_rect = texte_surface.get_rect(center=(x + largeur // 2, y + hauteur // 2))
        self.fenetre.blit(texte_surface, texte_rect)

    def gestion_evenement(self, evenements):
        for event in evenements:
            global play_sound1, play_sound2
            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                if self.x_bouton < x < self.x_bouton + self.largeur_bouton and self.y_bouton1 < y < self.y_bouton1 + self.hauteur_bouton:
                    self.couleur_bouton1 = self.couleur_bouton_survol
                    if not play_sound1:
                        mouse_over_button_sound.play()
                        play_sound1 = True
                else:
                    self.couleur_bouton1 = self.couleur_bouton_normal
                    play_sound1 = False
                if self.x_bouton < x < self.x_bouton + self.largeur_bouton and self.y_bouton2 < y < self.y_bouton2 + self.hauteur_bouton:
                    self.couleur_bouton2 = self.couleur_bouton_survol
                    if not play_sound2:
                        mouse_over_button_sound.play()
                        play_sound2 = True 
                else:
                    self.couleur_bouton2 = self.couleur_bouton_normal
                    play_sound2 = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if self.x_bouton < x < self.x_bouton + self.largeur_bouton and self.y_bouton1 < y < self.y_bouton1 + self.hauteur_bouton:
                    self.couleur_bouton1 = self.couleur_bouton_clic
                    launch_party_click_button_sound.play()
                    return "menu"

                if self.x_bouton < x < self.x_bouton + self.largeur_bouton and self.y_bouton2 < y < self.y_bouton2 + self.hauteur_bouton:
                    self.couleur_bouton2 = self.couleur_bouton_clic
                    pygame.quit()
                    sys.exit()

    def afficher(self):
            pygame.display.set_caption("Pokemon")
            self.fenetre.blit(self.image_fond, (0, 0))

            self.dessiner_bouton(self.x_bouton, self.y_bouton1, self.largeur_bouton, self.hauteur_bouton, "ACCUEIL", self.couleur_bouton1)
            self.dessiner_bouton(self.x_bouton, self.y_bouton2, self.largeur_bouton, self.hauteur_bouton, "QUITTER", self.couleur_bouton2)

            pygame.display.flip()

if __name__ == "__main__":
    jeu = PokemonGame()
    jeu.run()
