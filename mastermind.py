from random import randint
from art import tprint
from colorama import Fore, Style

"""
- générer une combinaison d'entiers aléatoire.
- demander les combinaisons à l'utilisateur (12 essais).
- comparer la combinaison de l'utilisateur avec celle de l'ordinateur.
- afficher le résultat de la combinaison (* noir bien placé ou 'o' blanc mal placé).
"""


# auteur : Baptiste Lacroix

def generer_combinaison():
    """
    elle génère 4 chiffres aléatoires qu'elle ajoute à la liste combinaisonIA.
    qu'elle retourne.
    """
    combinaisonIA = []
    for _ in range(1, 5):
        chiffreAlea = randint(1, 8)
        combinaisonIA.append(chiffreAlea)
    # print("Combinaison IA : ", combinaisonIA)
    return combinaisonIA


def combinaison_joueur(combinaisonOrdi):
    """
    elle demande 4 chiffres que le joueur va donner puis la fonction va les ajouter dans 
    une liste qu'elle retourne.
    """
    combinaisonJC = []
    for i in range(1, 5):
        chiffreJC = test_input(i)
        # tant que le chiffre n'est pas entre 1 et 8
        # Si le joueur entre le nombre "666" alors le code se lancera
        if chiffreJC == 666:
            print(Fore.RED)
            tprint(str(combinaisonOrdi))
            print(Style.RESET_ALL)
        while chiffreJC < 1 or chiffreJC > 8:
            chiffreJC = test_input(i)
        combinaisonJC.append(chiffreJC)
    return combinaisonJC


def test_input(i):
    while True:
        try:
            chiffreJC = int(input("Couleur " + str(i) + " : "))
            break
        except ValueError:
            print(Fore.RED)
            print("Erreur vous ne devez entrer que des chiffres compris entre 1 et 8 !")
            print(Style.RESET_ALL)
    return chiffreJC


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
        print(Fore.GREEN)
        tprint("Vous    avez    trouve    la    bonne    combinaison    !")
        print(Style.RESET_ALL)
        return
    else:
        for i in range(4):
            # pour chaque chiffre choisi par le joueur
            if combinaisonJC[i] == combinaisonIA[i]:
                # si le chiffre du joueur est au meme endroit dans la liste de l'ordi
                listeNoir.append(combinaisonJC[i])  # ajoute le chiffre a la listeNoir
        for i in range(4):
            if combinaisonJC[i] in combinaisonIA and combinaisonJC[i] not in listeNoir:
                # ieme element de combinaisonJC dans combinaisonIA
                # sinon si le chiffre du joueur est dans la liste de l'ordi mais mal placé
                listeBlanc.append(combinaisonJC[i])

    listeNoir = len(listeNoir) * noir
    listeBlanc = len(listeBlanc) * blanc
    print(Fore.LIGHTMAGENTA_EX + "chiffre(s) bien placé(s) : ", listeNoir, Fore.YELLOW + " / chiffre(s) mal placé(s) : "
          , listeBlanc + Style.RESET_ALL)
    # print("chiffre utilisés : ")
    # for i in combinaisonJC:
        # couleur_chiffres(i)

    """
def couleur_chiffres(chiffre):
    liste_chiffres = [1, 2, 3, 4, 5, 6, 7, 8]
    if chiffre == liste_chiffres[0]:
        print(Fore.WHITE + str(liste_chiffres[0]) + Style.RESET_ALL)  # Blanc
    elif chiffre == liste_chiffres[1]:
        print(Fore.BLUE + str(liste_chiffres[1]) + Style.RESET_ALL)  # Bleu
    elif chiffre == liste_chiffres[2]:
        print(Fore.GREEN + str(liste_chiffres[2]) + Style.RESET_ALL)  # Vert
    elif chiffre == liste_chiffres[3]:
        print(Fore.RED + str(liste_chiffres[3]) + Style.RESET_ALL)  # Rouge
    elif chiffre == liste_chiffres[4]:
        print(Fore.MAGENTA + str(liste_chiffres[4]) + Style.RESET_ALL)  # Rose
    elif chiffre == liste_chiffres[5]:
        print(Fore.BLACK + str(liste_chiffres[5]) + Style.RESET_ALL)  # Noir
    elif chiffre == liste_chiffres[6]:
        print(Fore.YELLOW + str(liste_chiffres[6]) + Style.RESET_ALL)  # Jaune
    elif chiffre == liste_chiffres[7]:
        print(Fore.CYAN + str(liste_chiffres[7]) + Style.RESET_ALL)  # bleu ciel
    """

def main():
    essaie = "essaie numéro : "
    print(Fore.MAGENTA)
    tprint("Bienvenue    dans    le    Mastermind    de    Baptiste.\n ")
    print(Style.RESET_ALL)
    nbr_essaies = 1
    print(Fore.BLUE + essaie + str(nbr_essaies) + Style.RESET_ALL)
    combinaisonOrdi = generer_combinaison()
    combinaisonPlayer = combinaison_joueur(combinaisonOrdi)
    verification(combinaisonOrdi, combinaisonPlayer)

    while combinaisonPlayer != combinaisonOrdi and nbr_essaies < 12:
        combinaisonPlayer = combinaison_joueur(combinaisonOrdi)
        verification(combinaisonOrdi, combinaisonPlayer)
        nbr_essaies = nbr_essaies + 1

        if nbr_essaies < 5:
            print(Fore.BLUE + essaie + str(nbr_essaies) + Style.RESET_ALL)
        elif 5 <= nbr_essaies <= 9:
            print(Fore.YELLOW + essaie + str(nbr_essaies) + Style.RESET_ALL)
        elif nbr_essaies > 9:
            print(Fore.RED + essaie + str(nbr_essaies) + Style.RESET_ALL)

    if nbr_essaies == 12:
        print(Fore.RED)
        tprint("Vous    avez    perdu    !")
        tprint("La  solution  etait  :  " + " ".join(str(combinaisonOrdi)))
        print(Style.RESET_ALL)


main()
