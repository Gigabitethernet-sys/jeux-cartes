import random
from Class.Cartes import Carte
class Deck:
    couleurs = ["Pique", "Coeur", "Carreau", "Trefle"]
    valeurs = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
               "Valet", "Dame", "Roi"
           ]

    def __init__(self):
        self.cartes = []
        for couleur in Deck.couleurs:
            for valeur in Deck.valeurs:
                self.cartes.append(Carte(valeur, couleur))

    def melanger(self):
        random.shuffle(self.cartes)