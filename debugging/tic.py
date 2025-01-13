#!/usr/bin/python3
def print_board(board):
    """
    Affiche le plateau de jeu sous forme de grille.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """
    Vérifie si un joueur a gagné.
    Retourne True si un joueur a trois symboles alignés, sinon False.
    """
    # Vérification des lignes
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Vérification des colonnes
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Vérification des diagonales
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def is_full(board):
    """
    Vérifie si le plateau est plein.
    Retourne True si toutes les cases sont remplies, sinon False.
    """
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    """
    Implémente le jeu du Tic Tac Toe pour deux joueurs.
    """
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)
        print(f"Tour du joueur {player}.")
        
        # Saisie et validation des entrées
        try:
            row = int(input("Entrez la ligne (0, 1 ou 2) : "))
            col = int(input("Entrez la colonne (0, 1 ou 2) : "))
            if row not in range(3) or col not in range(3):
                print("Les coordonnées doivent être entre 0 et 2. Réessayez.")
                continue
            if board[row][col] != " ":
                print("Cette case est déjà prise ! Réessayez.")
                continue
        except ValueError:
            print("Entrée invalide. Veuillez entrer des nombres entiers.")
            continue

        # Mettre à jour le plateau
        board[row][col] = player

        # Vérification du gagnant
        if check_winner(board):
            print_board(board)
            print(f"Félicitations ! Le joueur {player} a gagné !")
            break

        # Vérification du match nul
        if is_full(board):
            print_board(board)
            print("Match nul ! Le plateau est plein.")
            break

        # Changer de joueur
        player = "O" if player == "X" else "X"

# Lancer le jeu
if __name__ == "__main__":
    tic_tac_toe()
