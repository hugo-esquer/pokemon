import pygame
from menu import menu_ppl
from pokedex import pokedex
from game import game
from combat import combat

pygame.init()
# Paramètres de la fenêtre
largeur_fenetre = 800
hauteur_fenetre = 480
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))

menu = menu_ppl(fenetre)
pokedex_menu = pokedex(fenetre)
game_menu = game(fenetre)

ecran_actuel = menu  # Commencez à l'écran d'accueil

en_cours = True
while en_cours:
    evenements = pygame.event.get()
    for event in evenements:
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Gestion des événements et affichage en fonction de l'écran actuel
    prochain_ecran = ecran_actuel.gestion_evenement(evenements)
    ecran_actuel.afficher()

    # Logique pour changer d'écran
    if prochain_ecran == "menu":
        ecran_actuel = menu
    if prochain_ecran == "pokedex_menu":
        ecran_actuel = pokedex_menu
    if prochain_ecran == "game_menu":
        ecran_actuel = game_menu
    if prochain_ecran == "combat":
        joueur = game_menu.obtenir_selection()
        ecrant_combat = combat(fenetre, joueur)
        ecran_actuel = ecrant_combat

    pygame.display.flip()
