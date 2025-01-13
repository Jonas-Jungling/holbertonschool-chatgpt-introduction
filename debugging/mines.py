#!/usr/bin/python3
import random
import os

def effacer_ecran():
    os.system('cls' if os.name == 'nt' else 'clear')

class Demineur:
    def __init__(self, largeur=10, hauteur=10, mines=10):
        self.largeur = largeur
        self.hauteur = hauteur
        self.mines = set(random.sample(range(largeur * hauteur), mines))
        self.grille = [[' ' for _ in range(largeur)] for _ in range(hauteur)]
        self.revele = [[False for _ in range(largeur)] for _ in range(hauteur)]
        self.total_cases = largeur * hauteur
        self.cases_non_minees = self.total_cases - mines
        self.cases_revelees = 0

    def afficher_grille(self, tout_reveler=False):
        effacer_ecran()
        print('  ' + ' '.join(str(i) for i in range(self.largeur)))
        for y in range(self.hauteur):
            print(y, end=' ')
            for x in range(self.largeur):
                if tout_reveler or self.revele[y][x]:
                    if (y * self.largeur + x) in self.mines:
                        print('*', end=' ')
                    else:
                        compte = self.compter_mines_voisines(x, y)
                        print(compte if compte > 0 else ' ', end=' ')
                else:
                    print('.', end=' ')
            print()

    def compter_mines_voisines(self, x, y):
        compteur = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.largeur and 0 <= ny < self.hauteur:
                    if (ny * self.largeur + nx) in self.mines:
                        compteur += 1
        return compteur

    def reveler(self, x, y):
        if (y * self.largeur + x) in self.mines:
            return False
        if not self.revele[y][x]:  # Éviter de compter plusieurs fois une même case
            self.revele[y][x] = True
            self.cases_revelees += 1
        if self.compter_mines_voisines(x, y) == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.largeur and 0 <= ny < self.hauteur and not self.revele[ny][nx]:
                        self.reveler(nx, ny)
        return True

    def jouer(self):
        while True:
            self.afficher_grille()
            if self.cases_revelees == self.cases_non_minees:
                self.afficher_grille(tout_reveler=True)
                print("Félicitations ! Vous avez gagné !")
                break
            try:
                x = int(input("Entrez la coordonnée x : "))
                y = int(input("Entrez la coordonnée y : "))
                if not self.reveler(x, y):
                    self.afficher_grille(tout_reveler=True)
                    print("Game Over ! Vous avez touché une mine.")
                    break
            except ValueError:
                print("Entrée invalide. Veuillez entrer uniquement des nombres.")

if __name__ == "__main__":
    jeu = Demineur()
    jeu.jouer()
