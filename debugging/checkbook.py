#!/usr/bin/env python3

class Checkbook:
    """
    Classe représentant un carnet de chèques avec des fonctionnalités pour déposer, retirer de l'argent
    et consulter le solde.
    """
    def __init__(self):
        """
        Initialise un nouveau carnet de chèques avec un solde de départ de 0.0.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Dépose un montant sur le compte.

        Paramètres:
        amount (float): Montant à déposer.

        Résultat:
        Le solde est mis à jour et le montant déposé est affiché.
        """
        self.balance += amount
        print("Dépôt effectué : ${:.2f}".format(amount))
        print("Solde actuel : ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Retire un montant du compte si le solde est suffisant.

        Paramètres:
        amount (float): Montant à retirer.

        Résultat:
        Si le solde est suffisant, il est mis à jour et le montant retiré est affiché.
        Sinon, un message d'erreur est affiché.
        """
        if amount > self.balance:
            print("Fonds insuffisants pour effectuer ce retrait.")
        else:
            self.balance -= amount
            print("Retrait effectué : ${:.2f}".format(amount))
            print("Solde actuel : ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Affiche le solde actuel du compte.
        """
        print("Solde actuel : ${:.2f}".format(self.balance))


def main():
    """
    Fonction principale pour interagir avec l'utilisateur.
    Permet de choisir des actions (dépôt, retrait, solde ou quitter) et gère les erreurs d'entrée.
    """
    cb = Checkbook()
    while True:
        action = input("Que souhaitez-vous faire ? (deposit, withdraw, balance, exit) : ")
        if action.lower() == 'exit':
            print("Merci d'avoir utilisé le carnet de chèques. Au revoir !")
            break
        elif action.lower() == 'deposit':
            try:
                amount = float(input("Entrez le montant à déposer : $"))
                if amount < 0:
                    print("Le montant à déposer doit être positif.")
                else:
                    cb.deposit(amount)
            except ValueError:
                print("Entrée invalide. Veuillez entrer un montant numérique.")
        elif action.lower() == 'withdraw':
            try:
                amount = float(input("Entrez le montant à retirer : $"))
                if amount < 0:
                    print("Le montant à retirer doit être positif.")
                else:
                    cb.withdraw(amount)
            except ValueError:
                print("Entrée invalide. Veuillez entrer un montant numérique.")
        elif action.lower() == 'balance':
            cb.get_balance()
        else:
            print("Commande invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
