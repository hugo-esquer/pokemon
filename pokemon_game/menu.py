import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Paramètres de la fenêtre
largeur_fenetre = 800
hauteur_fenetre = 480

# Couleurs
couleur_fond = (255, 255, 255)
couleur_bouton = (0, 128, 255)
couleur_texte = (255, 255, 255)

# Création de la fenêtre
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("Pokemon")

# Fonction pour dessiner un bouton
def dessiner_bouton(x, y, largeur, hauteur, texte):
    pygame.draw.rect(fenetre, couleur_bouton, (x, y, largeur, hauteur))
    
    font = pygame.font.SysFont('Bombardier', 24)
    texte_surface = font.render(texte, True, couleur_texte)
    texte_rect = texte_surface.get_rect(center=(x + largeur // 2, y + hauteur // 2))
    
    fenetre.blit(texte_surface, texte_rect)

# Obtenir les dimensions du bouton
largeur_bouton = 300
hauteur_bouton = 50

# Calculer les positions des boutons pour les centrer
x_bouton = (largeur_fenetre - largeur_bouton) // 2
y_bouton1 = (hauteur_fenetre - 3 * hauteur_bouton) // 4
y_bouton2 = y_bouton1 + hauteur_bouton + (hauteur_fenetre - 3 * hauteur_bouton) // 4
y_bouton3 = y_bouton2 + hauteur_bouton + (hauteur_fenetre - 3 * hauteur_bouton) // 4

# Boucle principale
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    fenetre.fill(couleur_fond)

    # Dessiner les boutons
    dessiner_bouton(x_bouton, y_bouton1, largeur_bouton, hauteur_bouton, "LANCER UNE PARTIE")
    dessiner_bouton(x_bouton, y_bouton2, largeur_bouton, hauteur_bouton, "ACCEDER AU POKEDEX")
    dessiner_bouton(x_bouton, y_bouton3, largeur_bouton, hauteur_bouton, "AJOUTER UN POKEMON")

    pygame.display.flip()
