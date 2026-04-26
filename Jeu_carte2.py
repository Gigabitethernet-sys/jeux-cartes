import random

from Class.Cartes import Carte
from Class.Deck import Deck

deck = Deck()
deck.melanger()

cartes_selectionnees = deck.cartes[0:10]

cartes_memory = cartes_selectionnees + cartes_selectionnees
random.shuffle(cartes_memory)

#début du jeu - Joueur choisit 2 cartes
cartes_enlevees = []
nb_coups = 0
while len(cartes_enlevees) < 20:
    #plateau
    print("---- Plateau ----")

    for i in range(20):
        if cartes_memory[i] in cartes_enlevees:
            print(f"{i}: [trouvée]", end="  ")
        else:
            print(f"{i}: [?]", end="")
        if i==4 or i == 9 or i == 14:
            print("")
            print("")

    print("")
    print("")
    Choix1 = int(input("Choisissez la première carte (0-19) : "))
    while Choix1 < 0 or Choix1 > 19 or cartes_memory[Choix1] in cartes_enlevees:
        if Choix1 < 0 or Choix1 > 19:
            print("On a dit entre 0 et 19 Einstein")
        else:
            print("Cette carte a déjà été trouvée")
        Choix1 = int(input("Choisis les cartes que tu souhaites retourner dépêche-toi : "))


    Choix2 = int(input("Choisissez la deuxième carte (0-19) : "))
    while Choix2 < 0 or Choix2 > 19 or Choix2 == Choix1 or cartes_memory[Choix2] in cartes_enlevees:
        if Choix2 < 0 or Choix2 > 19:
            print("Choisis un numéro entre 0 et 19 !")
        elif Choix2 == Choix1:
            print("Tu peux pas choisir 2 fois la même carte")
        else:
            print("Cette carte a déjà été trouvée")
        Choix2 = int(input("Choisissez la deuxième carte (0-19) : "))
    nb_coups += 1

    carte1 = cartes_memory[Choix1]
    carte2 = cartes_memory[Choix2]

    print("La carte 1 est : ", carte1)
    print("La carte 2 est : ", carte2)

    if cartes_memory[Choix1].valeur == cartes_memory[Choix2].valeur:
        print("Paire trouvée !")
        cartes_enlevees.append(carte1)
        cartes_enlevees.append(carte2)
    else:
        print("Les 2 cartes ne correspondent pas ! Retente ta chance looser")

print("Magnifique tié un monstre bravo tia gagné")
print("Tu as gagné en", nb_coups, "coups !")
