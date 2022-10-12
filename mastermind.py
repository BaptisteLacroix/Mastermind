from random import randint
from art import tprint
from colorama import Fore, Style
from typing import List, Dict

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
    :return: liste de l'ordi
    """
    combinaisonIA: List[int] = []
    for _ in range(1, 5):
        chiffreAlea = randint(1, 8)
        combinaisonIA.append(chiffreAlea)
    # print("Combinaison IA : ", combinaisonIA)
    return combinaisonIA


def combinaison_joueur(combinaisonOrdi: List[int]) -> List[int]:
    """
    elle demande 4 chiffres que le joueur va donner puis la fonction va les ajouter dans 
    une liste qu'elle retourne.
    :param combinaisonOrdi: liste de l'ordi
    :return: liste du joueur
    """
    combinaisonJC: List[int] = []
    for i in range(1, 5):
        chiffreJC: int = test_input(i)
        # tant que le chiffre n'est pas entre 1 et 8
        # Si le joueur entre le nombre "666" alors le code se lancera
        if chiffreJC == 666:
            print(Fore.RED)
            tprint(str(combinaisonOrdi))
            print(Style.RESET_ALL)
        while chiffreJC < 1 or chiffreJC > 8:
            chiffreJC: int = test_input(i)
        combinaisonJC.append(chiffreJC)
    return combinaisonJC


def test_input(i: int) -> int:
    """
    la fonction va demander à l'utilisateur de rentrer un chiffre.
    :param i: numéro du chiffre
    :return: chiffre
    """
    while True:
        try:
            chiffreJC: int = int(input("Couleur " + str(i) + " : "))
            break
        except ValueError:
            print(Fore.RED)
            print("Erreur vous ne devez entrer que des chiffres compris entre 1 et 8 !")
            print(Style.RESET_ALL)
    return chiffreJC


def verification(combinaisonIA: List[int], combinaisonJC: List[int]) -> None:
    """
    la fontion va vérifier si les chiffres du joueur correspondent
    aux chiffres de l'ordinateur.

    la fonction va vérifier si un des chiffres du joueur se situe bien dans la liste.
    Si le chiffre se trouve dans la liste de l'ordi on va ajouter le chiffre à la listeBlanc.
    :param combinaisonIA: liste de l'ordi
    :param combinaisonJC: liste du joueur
    :return: None
    """

    noir: str = '*'
    blanc: str = 'o'
    dict_nbr_elemets_BOT: Dict[str, int] = {}  # {numéro, nombre de fois qu'il est présent} pour le BOT
    dict_nbr_elemets_JC: Dict[str, int] = {}  # {numéro, nombre de fois qu'il est présent} pour le Joueur
    # compte le nombre de fois que l'élément est présent dans la liste
    for element in combinaisonIA:
        if element in dict_nbr_elemets_BOT:
            dict_nbr_elemets_BOT[str(element)] += 1
        else:
            dict_nbr_elemets_BOT[str(element)] = 1
    liste_noir: List[int] = []  # chiffre bien placé
    liste_blanc: List[int] = []  # contiendra les chiffres mal placés

    if combinaisonJC == combinaisonIA:
        # si la liste choisie est la meme que celle de l'ordi alors :
        print(Fore.GREEN)
        tprint("Vous    avez    trouve    la    bonne    combinaison    !")
        print(Style.RESET_ALL)
        print("La  solution  etait  :  " + " ".join(str(combinaisonIA)))
    else:
        for i in range(4):
            # pour chaque chiffre choisi par le joueur
            if combinaisonJC[i] == combinaisonIA[i]:
                # si le chiffre du joueur est au meme endroit dans la liste de l'ordi
                liste_noir.append(combinaisonJC[i])  # ajoute le chiffre a la listeNoir
                # On compte +1 dans le dictionnaire pour le chiffre trouvé
                if combinaisonJC[i] in dict_nbr_elemets_JC:
                    dict_nbr_elemets_JC[str(combinaisonJC[i])] += 1
                else:
                    dict_nbr_elemets_JC[str(combinaisonJC[i])] = 1
        for j in range(4):
            if combinaisonJC[j] in combinaisonIA and liste_noir.count(combinaisonJC[j]) < dict_nbr_elemets_BOT[
                str(combinaisonJC[j])]:
                # si le chiffre du joueur se trouve dans la liste de l'ordi
                liste_blanc.append(combinaisonJC[j])  # ajoute le chiffre a la listeBlanc

        taille_liste_noir = len(liste_noir) * noir
        taille_liste_blanc = len(liste_blanc) * blanc
        print(Fore.LIGHTMAGENTA_EX + "chiffre(s) bien placé(s) : ", taille_liste_noir, Fore.YELLOW +
              " / chiffre(s) mal placé(s) : ", taille_liste_blanc + Style.RESET_ALL)


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


if __name__ == "__main__":
    main()
