import pygame
import sys

pygame.init()

surfaceW, surfaceH = 800, 480

class Menu:
    def __init__(self, application, *groupes):
        self.couleurs = {'normal': (255, 165, 0), 'survol': (173, 21, 230)}
        font = pygame.font.SysFont('Bombardier', 24)
        items = [('JOUER', application.jeu), ('QUITTER', application.quitter)]
        x, y = 400, 200
        self._boutons = [MenuBouton(texte, self.couleurs['normal'], font, x, y + i * 120, 200, 50, cmd) for i, (texte, cmd) in enumerate(items)]
        for bouton in self._boutons:
            for groupe in groupes:
                groupe.add(bouton)

    def update(self, events):
        clicGauche, *_ = pygame.mouse.get_pressed()
        posPointeur = pygame.mouse.get_pos()
        for bouton in self._boutons:
            if bouton.rect.collidepoint(*posPointeur):
                pygame.mouse.set_cursor(*pygame.cursors.tri_left)
                bouton.dessiner(self.couleurs['survol'])
                if clicGauche:
                    bouton.executerCommande()
                break
            else:
                bouton.dessiner(self.couleurs['normal'])
        else:
            pygame.mouse.set_cursor(*pygame.cursors.arrow)

    def detruire(self):
        pygame.mouse.set_cursor(*pygame.cursors.arrow)

class MenuBouton(pygame.sprite.Sprite):
    def __init__(self, texte, couleur, font, x, y, largeur, hauteur, commande):
        super().__init__()
        self._commande = commande
        self.image = pygame.Surface((largeur, hauteur))
        self.rect = self.image.get_rect(center=(x, y))
        self.texte = font.render(texte, True, (0, 0, 0))
        self.rectTexte = self.texte.get_rect(center=(largeur / 2, hauteur / 2))
        self.couleur = couleur
        self.dessiner(couleur)

    def dessiner(self, couleur):
        self.image.fill(couleur)
        self.image.blit(self.texte, self.rectTexte)

    def executerCommande(self):
        self._commande()

class Jeu:
    def __init__(self, jeu, *groupes):
        self._fenetre = jeu.fenetre
        jeu.fond = (0, 0, 0)
        couleurs = [(0, 48, i) for i in range(0, 256, 15)] + sorted([(0, 48, i) for i in range(0, 256, 15)][1:-1], reverse=True)
        self._couleurTexte = iter(couleurs)
        self._font = pygame.font.SysFont('Helvetica', 36, bold=True)
        self.creerTexte()
        self.rectTexte = self.texte.get_rect(center=(surfaceW / 2, surfaceH / 2))
        self._CLIGNOTER = pygame.USEREVENT + 1
        pygame.time.set_timer(self._CLIGNOTER, 80)

    def creerTexte(self):
        self.texte = self._font.render('LE JEU EST EN COURS D\'EXÉCUTION', True, next(self._couleurTexte))

    def update(self, events):
        self._fenetre.blit(self.texte, self.rectTexte)
        for event in events:
            if event.type == self._CLIGNOTER:
                self.creerTexte()
                break

    def detruire(self):
        pygame.time.set_timer(self._CLIGNOTER, 0)

class Application:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Pokemon")
        image_fond = pygame.image.load("pokemon_game\\images\\background.accueil.jpg")
        self.fond = pygame.transform.scale(image_fond, (surfaceW, surfaceH))
        self.fenetre = pygame.display.set_mode((surfaceW, surfaceH))
        self.groupeGlobal = pygame.sprite.Group()
        self.statut = True

    def _initialiser(self):
        try:
            self.ecran.detruire()
            self.groupeGlobal.empty()
        except AttributeError:
            pass

    def menu(self):
        self._initialiser()
        self.ecran = Menu(self, self.groupeGlobal)

    def jeu(self):
        self._initialiser()
        self.ecran = Jeu(self, self.groupeGlobal)

    def quitter(self):
        self.statut = False

    def update(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.quitter()
                return
        self.fenetre.blit(self.fond, (0, 0))
        self.ecran.update(events)
        self.groupeGlobal.update()
        self.groupeGlobal.draw(self.fenetre)
        pygame.display.update()

app = Application()
app.menu()

clock = pygame.time.Clock()

while app.statut:
    app.update()
    clock.tick(30)

pygame.quit()
sys.exit()
