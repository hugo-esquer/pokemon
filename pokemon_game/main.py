import pygame
import sys
import subprocess

# Initialisation de Pygame
pygame.init()

# Paramètres de la fenêtre
largeur_fenetre = 800
hauteur_fenetre = 480

# Image de fond
image_fond = pygame.image.load("pokemon_game\\images\\background.accueil.jpg")
image_fond = pygame.transform.scale(image_fond, (largeur_fenetre, hauteur_fenetre))

# Couleurs
couleur_bouton_normal = (255, 165, 0)
couleur_bouton_survol = (255, 200, 0)
couleur_bouton_clic = (255, 100, 0)
couleur_texte = (0, 0, 0)

# Création de la fenêtre
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("Pokemon")

# Fonction pour dessiner un bouton
def dessiner_bouton(x, y, largeur, hauteur, texte, couleur):
    pygame.draw.rect(fenetre, couleur, (x, y, largeur, hauteur))
    
    font = pygame.font.SysFont('Bombardier', 24)
    texte_surface = font.render(texte, True, couleur_texte)
    texte_rect = texte_surface.get_rect(center=(x + largeur // 2, y + hauteur // 2))
    
    fenetre.blit(texte_surface, texte_rect)

# Obtenir les dimensions du bouton
largeur_bouton = 300
hauteur_bouton = 50

# Calculer les positions des boutons pour les centrer
x_bouton = (largeur_fenetre - largeur_bouton) // 2
y_bouton1 = (hauteur_fenetre - (hauteur_bouton * 2 + 10)) // 2
y_bouton2 = y_bouton1 + hauteur_bouton + 60
# Définir la couleur initiale des boutons
couleur_bouton1 = couleur_bouton_normal
couleur_bouton2 = couleur_bouton_normal

# Boucle principale
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Gérer les événements de la souris pour changer la couleur des boutons
        if event.type == pygame.MOUSEMOTION:
            x, y = event.pos
            if x_bouton < x < x_bouton + largeur_bouton and y_bouton1 < y < y_bouton1 + hauteur_bouton:
                couleur_bouton1 = couleur_bouton_survol
            else:
                couleur_bouton1 = couleur_bouton_normal

            if x_bouton < x < x_bouton + largeur_bouton and y_bouton2 < y < y_bouton2 + hauteur_bouton:
                couleur_bouton2 = couleur_bouton_survol
            else:
                couleur_bouton2 = couleur_bouton_normal


        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if x_bouton < x < x_bouton + largeur_bouton and y_bouton1 < y < y_bouton1 + hauteur_bouton:
                couleur_bouton1 = couleur_bouton_clic

            if x_bouton < x < x_bouton + largeur_bouton and y_bouton2 < y < y_bouton2 + hauteur_bouton:
                couleur_bouton2 = couleur_bouton_clic


    fenetre.blit(image_fond, (0, 0))

    # Dessiner les boutons
    dessiner_bouton(x_bouton, y_bouton1, largeur_bouton, hauteur_bouton, "ACCUEIL", couleur_bouton1)
    dessiner_bouton(x_bouton, y_bouton2, largeur_bouton, hauteur_bouton, "QUITTER", couleur_bouton2)
    

    pygame.display.flip()
