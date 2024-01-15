import pygame
import sys

pygame.init()

#fenetre de jeu

fenêtre = pygame.display.set_mode(600,600)
pygame.display.set_caption ("Pokemon")


#charge le background
background = pygame.image.load()

#boucle principale du jeu 

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

fenêtre.blit (, (0,0))
pygame.display.flip()


pygame.quit
sys.exit