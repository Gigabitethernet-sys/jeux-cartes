import random
from Class.Cartes import Carte
from Class.Deck import Deck

def calculer_score(main):
    score = 0
    for carte in main:
        if carte.valeur in ["Valet", "Dame", "Roi"]:
            score += 10
        elif carte.valeur == "1":
            score += 11
        else:
            score += int(carte.valeur)
    return score

argent = 1000
jouer = True

while argent > 0 and jouer:
    print("")
    print("=" * 40)

    print("Tu as", argent, "€")
    print("")

    deck = Deck()
    deck.melanger()

    mise = int(input("Combien veux-tu miser ? "))
    while mise > argent:
        print("Tu n'as que", argent, "€ sale pauvre tu veux t'endetter espèce d'inconscient ?")
        mise = int(input("Combien veux-tu miser ? "))
    print("")

    #Distribution
    main_joueur = []
    main_ordi = []

    main_joueur.append(deck.cartes.pop(0))
    main_ordi.append(deck.cartes.pop(0))
    main_joueur.append(deck.cartes.pop(0))
    main_ordi.append(deck.cartes.pop(0))

    print("---BLACKJACK---")
    print("")

    #tour joueur
    continuer = True
    while continuer:
        print("Tes cartes: ")
        for carte in main_joueur:
            print("-", carte)

        score_joueur = calculer_score(main_joueur)
        print("Ton score : ", score_joueur)
        print("")

        if score_joueur > 21:
            print("Ton score : ", score_joueur)
            print("Tu perds", mise, "€")
            argent -= mise
            continuer = False
            break

        choix = input("Veux-tu tirer une carte ? (oui/non) : ")

        if choix == "oui":
            main_joueur.append(deck.cartes.pop(0))
        else:
            continuer = False

    print("")

    #Tour ordinateur
    if score_joueur <= 21:
        print("---Tour de l'ordinateur---")

        while calculer_score(main_ordi) < 17:
            print("L'ordi tire une carte...")
            main_ordi.append(deck.cartes.pop(0))

        print("Cartes de l'ordi : ")
        for carte in main_ordi:
            print("-", carte)

        score_ordi = calculer_score(main_ordi)
        print("Score de l'ordi : ", score_ordi)
        print("")

    #Comparaison scores
        if score_ordi > 21:
            print("L'ordi a dépassé 21 ! T'as gagné gros clown")
            print("Tu gagnes", mise, "€ !")
            argent += mise
        elif score_joueur > score_ordi:
            print("T'as malheureusement gagné")
            print("Tu gagnes", mise, "€ !")
            argent += mise
        elif score_ordi > score_joueur:
            print("L'ordi a gagné sale gros looser ahahahahahaha")
            print("Tu perds", mise, "€")
            argent -= mise
        else:
            print("Egalité bouffon !")

    print("")
    print("Tu as maintenant", argent, "€")

    rejouer = input("Veux-tu rejouer ? (oui/non) : ")
    if rejouer != "oui":
        jouer = False
        print("Tu te retires avec", argent, "€")

print("")
if argent <= 0:
    print("T'as plus un centime retourne taffer avec Christine de la compta mon grand")
else:
    print("À bientôt !")