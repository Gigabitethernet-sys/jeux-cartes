import random
from Class.Cartes import Carte
from Class.Deck import Deck

def afficher_main(main):
    for i in range(len(main)):
        print(f"{i}: {main[i]}")

#Si une carte peut être posée
def poser_carte(carte, carte_table):
    if carte.couleur == carte_table.couleur or carte.valeur == carte_table.valeur:
        return True
    return False

#Si utilisateur a une carte jouable
def a_carte_jouable(main, carte_table):
    for carte in main:
        if poser_carte(carte, carte_table):
            return True
    return False

#Si ordi a une carte jouable
def ordi_joue(main_ordi, carte_table):
    for i in range(len(main_ordi)):
        if poser_carte(main_ordi[i], carte_table):
            return i
    return None

deck = Deck()
deck.melanger()
main_joueur = []
main_ordi = []

for i in range(7):
    main_joueur.append(deck.cartes.pop(0))
    main_ordi.append(deck.cartes.pop(0))

#carte sur la table
carte_table = deck.cartes.pop(0)

print("Distribution terminée !")
print("Vous avez 7 cartes chacun.")
print("")

#boucle début du jeu
tour = 0
while len(main_joueur) > 0 and len(main_ordi) > 0:
    tour += 1
    print("=" * 50)
    print(f"TOUR {tour}")
    print("=" * 50)
    print("")
    print("Carte sur la table :", carte_table)
    print("")
    print("Tes cartes :")
    afficher_main(main_joueur)
    print("")
    print(f"L'ordinateur a {len(main_ordi)} cartes")
    print("")

#Tour joueur
    if a_carte_jouable(main_joueur, carte_table):
        choix = int(input("Quelle carte veux-tu jouer ? (numéro) : "))


        while choix < 0 or choix >= len(main_joueur):
            print(f"Choisis un numéro entre 0 et {len(main_joueur) - 1} !")
            choix = int(input("Quelle carte veux-tu jouer ? (numéro) : "))

            #vérifier si carte valide
        while not poser_carte(main_joueur[choix], carte_table):
            print("Cette carte ne peut pas être jouée !")
            print("Tu dois jouer une carte de même couleur ou même valeur.")
            choix = int(input("Quelle carte veux-tu jouer ? (numéro) : "))

            while choix < 0 or choix >= len(main_joueur):
                print(f"Choisis un numéro entre 0 et {len(main_joueur) - 1} !")
                choix = int(input("Quelle carte veux-tu jouer ? (numéro) : "))

        carte_jouee = main_joueur.pop(choix)
        carte_table = carte_jouee
        print(f"Tu as joué : {carte_jouee}")
        print("")

    else:
        print("Tu n'as aucune carte jouable ! Pioche une carte.")

    #Cartes restantes dans le deck
        if len(deck.cartes) > 0:
            carte_piochee = deck.cartes.pop(0)
            main_joueur.append(carte_piochee)
            print(f"Tu as pioché : {carte_piochee}")
        else:
            print("Plus de cartes dans la pioche !")
        print("")

    #Victoire de l'utilisateur
    if len(main_joueur) == 0:
        print("Bravo pour la victoire")
        break

    print(f"Il te reste {len(main_joueur)} carte(s)")
    print("")
    input("Appuie sur Entrée pour continuer...")
    print("")

    #Tour de l'ordinateur
    print("--- Tour de l'ordinateur ---")
    print("")

    if a_carte_jouable(main_ordi, carte_table):
        index_carte = ordi_joue(main_ordi, carte_table)
        carte_jouee_ordi = main_ordi.pop(index_carte)
        carte_table = carte_jouee_ordi
        print(f"L'ordinateur joue : {carte_jouee_ordi}")
        print("")
    else:
        print("L'ordinateur n'a aucune carte jouable ! Il pioche.")

    #Cartes restantes dans le deck
        if len(deck.cartes) > 0:
            main_ordi.append(deck.cartes.pop(0))
            print("L'ordinateur a pioché une carte.")
        else:
            print("Plus de cartes dans la pioche !")
        print("")

    #Victoire ordinateur
    if len(main_ordi) == 0:
        print("L'ordinateur a gagné ! (perdre contre un ordinateur alors qu'on est ingénieur c'est un peu la honte honnêtement)")
        break

    print(f"L'ordinateur a {len(main_ordi)} carte")
    print("")

print("")
print("--- Fin de partie ---")

if len(main_joueur) == 0:
    print("Bravo !")
elif len(main_ordi) == 0:
    print("Perdu !!")
else:
    print("Fin de partie, il n'y a plus de cartes")