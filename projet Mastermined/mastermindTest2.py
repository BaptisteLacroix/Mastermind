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


def verification(combinaisonIA, combinaisonJC):
    """
    la fontion va vérifier si les chiffres du joueur correspondent
    aux chiffres de l'ordinateur.

    la fonction va vérifier si un des chiffres du joueur se situe bien dans la liste.
    Si le chiffre se trouve dans la liste de l'ordi on va ajouter le chiffre à la listeBlanc.
    """
    noir = '*'
    blanc = 'o'
    listeNoir = []  # contiendra les chiffres bien placés
    listeBlanc = []  # contiendra les chiffres mal placés

    if combinaisonJC == combinaisonIA:
        # si la liste choisie est la meme que celle de l'ordi alors :
        print("Vous avez trouvé la bonne combinaison")
    else:
        for i in range(4):
            # pour chaque chiffre choisi par le joueur
            if combinaisonJC[i] == combinaisonIA[i]:
                # si le chiffre du joueur est au meme endroit dans la liste de
                # l'ordi
                # ajoute le chiffre a la listeNoir
                listeNoir.append(combinaisonJC[i])
            elif combinaisonIA.count(combinaisonJC[i]) > listeBlanc.count(combinaisonJC[i]) + listeNoir.count(combinaisonJC[i]) + 1:
                # sinon si le ieme element de combinaisonJC est dans combinaisonIA et n'a pas ete comptabilise trop de fois
                # il faut que le nombre d'apparition de cet element dans la liste de l'IA soit inferieur ou egal au nombre
                # d'apparition de ce meme element dans les deux listes de noirs
                # et blancs
                listeBlanc.append(combinaisonJC[i])

        listeNoir = len(listeNoir) * noir
        listeBlanc = len(listeBlanc) * blanc
        print("chiffres bien placé : ", listeNoir, "et chiffre mal placé : ", listeBlanc)


def main():
    global combinaisonOrdi
    print("Bienvenue dans le Mastermind de Baptiste et Saif. ☺☻♥♦♣♠■ \n ")
    nbr_essaies = 0
    print("essaies numéro :", nbr_essaies)
    combinaisonOrdi = genererCombinaison()
    combinaisonPlayer = combinaisonJoueur()
    resultatCombinaison = verification(combinaisonOrdi, combinaisonPlayer)
    while combinaisonPlayer != combinaisonOrdi and nbr_essaies < 12:
        combinaisonPlayer = combinaisonJoueur()
        verification(combinaisonOrdi, combinaisonPlayer)
        nbr_essaies = nbr_essaies + 1
        print("essaies numéro :", nbr_essaies)
    if nbr_essaies == 12:
        print("Vous avez perdu ! La solution était :", combinaisonOrdi)

main()
