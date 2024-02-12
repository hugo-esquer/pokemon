import pygame
pygame.mixer.init()

# Chargement et initialisation audio
mouse_over_button_sound = pygame.mixer.Sound("pokemon_game/audio/bruitages/mouse_over_button.mp3")
mouse_over_button_sound.set_volume(0.25)
launch_party_click_button_sound = pygame.mixer.Sound("pokemon_game/audio/bruitages/launch_party_click_button.mp3")
pokedex_access_button_sound = pygame.mixer.Sound("pokemon_game/audio/bruitages/pokedex_access_click_button.mp3")
add_pokemon_button_sound = pygame.mixer.Sound("pokemon_game/audio/bruitages/adding_pokemon_click_button.mp3")
play_sound1 = False
play_sound2 = False
play_sound3 = False

# Boucle principale
class menu_ppl:
        
    def __init__(self, fenetre):
        self.fenetre = fenetre
        # Image de fond
        self.image_fond = pygame.image.load("pokemon_game/images/menu.pokemon.png")
        self.image_fond = pygame.transform.scale(self.image_fond, (800, 480))

        # Couleurs
        self.couleur_bouton_normal = (255, 165, 0)
        self.couleur_bouton_survol = (255, 200, 0)
        self.couleur_bouton_clic = (255, 100, 0)
        self.couleur_texte = (0, 0, 0)

        # Obtenir les dimensions du bouton
        self.largeur_bouton = 300
        self.hauteur_bouton = 50

        # Calculer les positions des boutons pour les centrer
        self.x_bouton = (800 - self.largeur_bouton) // 2
        self.y_bouton1 = (480 - 3 * self.hauteur_bouton) // 4
        self.y_bouton2 = self.y_bouton1 + self.hauteur_bouton + (480 - 3 * self.hauteur_bouton) // 4
        self.y_bouton3 = self.y_bouton2 + self.hauteur_bouton + (480 - 3 * self.hauteur_bouton) // 4

        # Définir la couleur initiale des boutons
        self.couleur_bouton1 = self.couleur_bouton_normal
        self.couleur_bouton2 = self.couleur_bouton_normal
        self.couleur_bouton3 = self.couleur_bouton_normal
    
    
    # Fonction pour dessiner un bouton
    def dessiner_bouton(self, x, y, largeur, hauteur, texte, couleur):
        pygame.draw.rect(self.fenetre, couleur, (x, y, largeur, hauteur))
        
        font = pygame.font.SysFont('Bombardier', 24)
        texte_surface = font.render(texte, True, self.couleur_texte)
        texte_rect = texte_surface.get_rect(center=(x + largeur // 2, y + hauteur // 2))
        
        self.fenetre.blit(texte_surface, texte_rect)

    def gestion_evenement(self, evenements):
        for event in evenements:
            global play_sound1, play_sound2, play_sound3
            # Gérer les événements de la souris pour changer la couleur des boutons
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
                if self.x_bouton < x < self.x_bouton + self.largeur_bouton and self.y_bouton3 < y < self.y_bouton3 + self.hauteur_bouton:
                    self.couleur_bouton3 = self.couleur_bouton_survol
                    if not play_sound3:
                        mouse_over_button_sound.play()
                        play_sound3 = True 
                else:
                    self.couleur_bouton3 = self.couleur_bouton_normal
                    play_sound3 = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if self.x_bouton < x < self.x_bouton + self.largeur_bouton and self.y_bouton1 < y < self.y_bouton1 + self.hauteur_bouton:
                    self.couleur_bouton1 = self.couleur_bouton_clic
                    launch_party_click_button_sound.play()
                    return "game_menu"

                if self.x_bouton < x < self.x_bouton + self.largeur_bouton and self.y_bouton2 < y < self.y_bouton2 + self.hauteur_bouton:
                    self.couleur_bouton2 = self.couleur_bouton_clic
                    pokedex_access_button_sound.play()
                    return "pokedex_menu"

                if self.x_bouton < x < self.x_bouton + self.largeur_bouton and self.y_bouton3 < y < self.y_bouton3 + self.hauteur_bouton:
                    self.couleur_bouton3 = self.couleur_bouton_clic
                    add_pokemon_button_sound.play()
                    return "ajout"

    def afficher(self):

        pygame.display.set_caption("Pokemon")
        self.fenetre.blit(self.image_fond, (0, 0))

        # Dessiner les boutons
        self.dessiner_bouton(self.x_bouton, self.y_bouton1, self.largeur_bouton, self.hauteur_bouton, "LANCER UNE PARTIE", self.couleur_bouton1)
        self.dessiner_bouton(self.x_bouton, self.y_bouton2, self.largeur_bouton, self.hauteur_bouton, "ACCEDER AU POKEDEX", self.couleur_bouton2)
        self.dessiner_bouton(self.x_bouton, self.y_bouton3, self.largeur_bouton, self.hauteur_bouton, "AJOUTER UN POKEMON", self.couleur_bouton3)

        pygame.display.flip()
