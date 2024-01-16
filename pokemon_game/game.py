import pygame
from models.menupokemon import menuPokemon

pygame.init()

largeur_fenetre = 800
hauteur_fenetre = 480
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("choisir un Pokémon")

NOIR = (0,0,0)

pokemon_joueur = ""
fond = pygame.image.load("pokemon_game\\images\\BG-selection.png")

menu_pokemon = menuPokemon(fond, "pokemon_game\\pokemon.json", largeur_fenetre, hauteur_fenetre, fenetre)
menu_pokemon.selection()