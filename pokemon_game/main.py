import pygame
from menu import menu_ppl
from pokedex import pokedex
from game import game
from combat import combat
from accueil import PokemonGame
from ajout_pokemon import PokemonApp

pygame.init()
# Paramètres de la fenêtre
largeur_fenetre = 800
hauteur_fenetre = 480
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))

accueil = PokemonGame(fenetre)
menu = menu_ppl(fenetre)
ajout = PokemonApp(fenetre)

ecran_actuel = accueil  # Commencez à l'écran d'accueil

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
        pokedex_menu = pokedex(fenetre)
        ecran_actuel = pokedex_menu
    if prochain_ecran == "game_menu":
        game_menu = game(fenetre)
        ecran_actuel = game_menu
    if prochain_ecran == "combat":
        joueur = game_menu.obtenir_selection()
        ecrant_combat = combat(fenetre, joueur)
        ecran_actuel = ecrant_combat
    if prochain_ecran == "ajout":
        ecran_actuel = ajout

    pygame.display.flip()
