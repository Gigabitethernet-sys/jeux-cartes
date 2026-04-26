class Carte:
    dico = {
        "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8,
        "9": 9, "10": 10, "Valet": 11, "Dame": 12, "Roi": 13
    }

    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

    def tour_gagne(self):
        return Carte.dico[self.valeur]

    def __str__(self):
        return self.valeur + " de " + self.couleur