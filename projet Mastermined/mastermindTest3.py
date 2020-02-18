from random import randint
from copy import deepcopy

"""
- générer une combinaison d'entiers aléatoire.
- demander les combinaisons à l'utilisateur (12 essais).
- comparer la combinaison de l'utilisateur avec celle de l'ordinateur.
- afficher le résultat de la combinaison (* noir bien placé ou 'o' blanc mal placé).
"""


def genererCombinaison():
    """
    elle génère 4 chiffres aléatoires qu'elle ajoute à la liste combinaisonIA.
    qu'elle retourne.
    """
    combinaisonIA = []
    for i in range(1, 5):
        chiffreAlea = randint(1, 8)
        combinaisonIA.append(chiffreAlea)
    print("Combinaison IA : ", combinaisonIA)
    return combinaisonIA


def combinaisonJoueur():
    """
    elle demande 4 chiffres que le joueur va donner puis la fonction va les ajouter dans
    une liste qu'elle retourne.
    """
    combinaisonJC = []
    for i in range(1, 5):
        chiffreJC = int(input("Couleur " + str(i) + " : "))
        # tant que le chiffre n'est pas entre 1 et 8
        # Si le joueur entre le nombre "666" alors le code se lancera
        if chiffreJC == 666:
            print("Vous venez d'activer le code de triche !",combinaisonOrdi)
        while chiffreJC < 1 or chiffreJC > 8:
            chiffreJC = int(input("Couleur " + str(i) + " : "))
        combinaisonJC.append(chiffreJC)
    return combinaisonJC


def blancs(combinaisonJC,combinaisonIA):
    i = 0
    mal_place = 0
    while i < pions:
        j = 0
        while j < pions:
            if combinaisonJC[i] == combinaisonIA[j]:
                mal_place = mal_place+1
                combinaisonJC[i] = 'y'
                combinaisonIA[j] = 'x'
                j = j+1
                i = i+1
    return mal_place

def noirs(combinaisonJC,combinaisonIA):
    bien_place = 0
    i = 0
    while i < pions:
        if combinaisonJC[i] == combinaisonIA[i]:
            bien_place = bien_place+1
            combinaisonJC[i] = 'y'
            combinaisonIA[i] = 'x'
            i = i+1
    return bien_place


def main():
    global combinaisonOrdi
    print("Bienvenue dans le Mastermind de Baptiste et Saif. ☺☻♥♦♣♠■ \n ")
    nbr_essaies = 0
    print("essaies numéro :", nbr_essaies)
    combinaisonOrdi = genererCombinaison()
    combinaisonPlayer = combinaisonJoueur()
    resultatCombinaisonBlancs = blancs(combinaisonJC,combinaisonIA)
    resultatCombinaisonNoirs = noirs(combinaisonJC,combinaisonIA):
    while combinaisonPlayer != combinaisonOrdi and nbr_essaies < 12:
        combinaisonPlayer = combinaisonJoueur()
        blancs(combinaisonJC,combinaisonIA) and noirs(combinaisonJC,combinaisonIA):
            nbr_essaies = nbr_essaies + 1
            print("essaies numéro :", nbr_essaies)
            if nbr_essaies == 12:
                print("Vous avez perdu ! La solution était :", combinaisonOrdi)
main()