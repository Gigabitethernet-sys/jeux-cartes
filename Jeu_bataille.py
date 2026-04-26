import random

from Class.Cartes import Carte
from Class.Deck import Deck

deck = Deck()
deck.melanger()
paquet = deck.cartes

J1 = paquet[0:26]
J2 = paquet[26:52]

#Pouvoirs spéciaux
espion_J1 = True  # Pouvoir d'espionner (1 fois par partie)
echange_J1 = True  # Pouvoir d'échanger (1 fois par partie)

print("J1 a", len(J1), "cartes")
print("J2 a", len(J2), "cartes")

tour = 0
while len(J1) > 0 and len(J2) > 0:
    tour += 1
    print("Tour", tour)

    if espion_J1 or echange_J1:
        print("\nPouvoirs disponibles :")
        if espion_J1:
            print("1. Espionner la carte de J2")
        if echange_J1:
            print("2. Échanger ta première carte avec une carte aléatoire de ton paquet")
        print("3. Ne rien faire")

        choix_pouvoir = input("Veux-tu utiliser un pouvoir ? (1/2/3) : ")

        if choix_pouvoir == "1" and espion_J1:
            print(f"La prochaine carte de J2 est : {J2[0]}")
            espion_J1 = False
            print("Pouvoir espion utilisé !\n")
        elif choix_pouvoir == "2" and echange_J1:
            if len(J1) > 1:
                index_aleatoire = random.randint(1, len(J1) - 1)
                J1[0], J1[index_aleatoire] = J1[index_aleatoire], J1[0]
                print("Carte échangée !")
                echange_J1 = False
                print("Pouvoir échange utilisé !\n")
        elif choix_pouvoir == "3":
            print("Aucun pouvoir utilisé.\n")

#Choix de la carte
    print("\nTes 3 premières cartes :")
    nb_cartes_affichees = min(3, len(J1))
    for i in range(nb_cartes_affichees):
        print(f"{i}: {J1[i]}")

    choix_carte = int(input(f"Quelle carte veux-tu jouer ? (0-{nb_cartes_affichees - 1}) : "))

    while choix_carte < 0 or choix_carte >= nb_cartes_affichees:
        print(f"Choisis entre 0 et {nb_cartes_affichees - 1} !")
        choix_carte = int(input(f"Quelle carte veux-tu jouer ? (0-{nb_cartes_affichees - 1}) : "))

        carte1 = J1.pop(choix_carte)

    carte2 = J2[0]
    J2.pop(0)

    print(f"\nJ1 joue : {carte1}")
    print(f"J2 joue : {carte2}")

#Parier
    pari = input("\nPenses-tu gagner ce tour ? (oui/non) : ")

    pli = [carte1, carte2]
    random.shuffle(pli)

    gagne_tour = False

    if carte1.tour_gagne() > carte2.tour_gagne():
        print("Le J1 gagne ce tour")
        J1.append(pli[0])
        J1.append(pli[1])
        gagne_tour = True

    elif carte1.tour_gagne() < carte2.tour_gagne():
        print("Le J2 gagne ce tour")
        J2.append(pli[0])
        J2.append(pli[1])
    else:
        print("Egalité")
        if len(J1) < 2 or len(J2) < 2:
            break
        C1 = J1.pop(0)
        C2 = J2.pop(0)
        C3 = J1.pop(0)
        C4 = J2.pop(0)
        if C3.tour_gagne() > C4.tour_gagne():
            J1 += [carte1, carte2, C1, C2, C3, C4]
            gagne_tour = True
        else:
            print("Le J2 gagne la bataille")
            J2 += [carte1, carte2, C1, C2, C3, C4]

#Vérification du pari
    if pari == "oui" and gagne_tour:
        print("Pari réussi, tu gagnes une carte bonus !")
        if len(J2) > 0:
            carte_bonus = J2.pop(0)
            J1.append(carte_bonus)
            print(f"Tu récupères : {carte_bonus}")
    elif pari == "oui" and not gagne_tour:
        print("Pari raté")


    print("Joueur 1 a", len(J1), "cartes")
    print("Joueur 2 a", len(J2), "cartes")
    print("--- Prochain tour ---")

if len(J1) == 52:
    print("Joueur 1 a gagné")
else:
    print("Joueur 2 a gagné")