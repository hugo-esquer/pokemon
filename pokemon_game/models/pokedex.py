import pygame
from menupokemon import menuPokemon

pygame.init()

largeur_fenetre = 800
hauteur_fenetre = 480
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("Pokédex")

NOIR = (0,0,0)

fond = pygame.image.load("pokemon_game\\images\\BG-dex.png")

menu_pokemon = menuPokemon(fond, largeur_fenetre, hauteur_fenetre, fenetre)
menu_pokemon.pokedex()