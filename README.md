# Jeux de Cartes en Python

Projet réalisé dans le cadre du BTS SIO 1 SISR dans le cadre de la matière introduction au développement.

## Description

Ce projet propose quatre jeux de cartes interactifs entièrement programmés en Python. Chaque jeu utilise une architecture orientée objet avec deux classes principales : `Carte` et `Deck`.

## Les Jeux

### 1. La Bataille

**Fichier :** `Jeu_bataille.py`

**Règles :**
- Jeu pour 2 joueurs (Joueur 1 vs Joueur 2)
- Le paquet de 52 cartes est mélangé et distribué équitablement (26 cartes chacun)
- À chaque tour, le joueur 1 peut :
  - **Choisir sa carte** : Sélectionner parmi ses 3 premières cartes
  - **Utiliser des pouvoirs spéciaux** (1 fois par partie chacun) :
    - **Espionner** : Voir la prochaine carte de l'adversaire
    - **Échanger** : Remplacer sa première carte par une carte aléatoire de son paquet
  - **Parier** : Prédire s'il va gagner le tour pour obtenir une carte bonus
- La carte la plus forte remporte les deux cartes qui sont ajoutées à la fin du paquet du gagnant
- En cas d'égalité : **Bataille !**
  - Chaque joueur pose une carte face cachée
  - Puis une carte face visible
  - La carte visible la plus forte remporte les 6 cartes
- Le jeu continue jusqu'à ce qu'un joueur ait plus de cartes que l'autre

**Valeurs des cartes :**
- 1 à 10 : valeur faciale
- Valet = 11
- Dame = 12
- Roi = 13

**Fonctionnalités interactives :**
- Choix de la carte à jouer parmi 3 options
- Pouvoirs spéciaux utilisables stratégiquement
- Système de pari avec récompense bonus
- Pause entre chaque tour pour suivre la partie

**Commande :**
```bash
python Jeu_bataille.py
```

### 2. Memory

**Fichier :** `Jeu_carte2.py`

**Règles :**
- Jeu de mémoire solo
- 20 cartes (10 paires) sont mélangées et posées face cachée
- Le joueur choisit deux cartes en entrant leur numéro (0-19)
- Si les deux cartes ont la même valeur : c'est une paire ! Elles restent visibles
- Sinon elles sont à nouveau cachées
- Le but est de retrouver toutes les paires en un minimum de coups

**Fonctionnalités :**
- Affichage du plateau avec les cartes trouvées et cachées
- Vérification que le joueur ne choisit pas deux fois la même carte
- Vérification que les numéros sont entre 0 et 19
- Compteur de coups pour mesurer la performance

**Commande :**
```bash
python Jeu_carte2.py
```

### 3. Blackjack

**Fichier :** `Blackjack.py`

**Règles :**
- Jeu contre l'ordinateur
- Vous misez une somme avant chaque manche
- Le but est de se rapprocher de 21 sans dépasser
- Distribution initiale : 2 cartes pour vous, 2 cartes pour l'ordinateur
- Vous pouvez tirer des cartes supplémentaires ou vous arrêter
- L'ordinateur tire automatiquement des cartes jusqu'à avoir au moins 17
- Comparaison des scores :
  - Si vous dépassez 21 : vous perdez votre mise
  - Si l'ordi dépasse 21 : vous gagnez votre mise
  - Sinon : le score le plus proche de 21 gagne
  - Égalité : vous récupérez votre mise

**Valeurs des cartes :**
- 1 (As) = 11 points
- 2 à 10 = valeur faciale
- Valet, Dame, Roi = 10 points

**Fonctionnalités :**
- Système de mise avec vérification du solde
- Manches illimitées tant que vous avez de l'argent
- Possibilité d'arrêter quand vous voulez
- Affichage du solde après chaque manche

**Commande :**
```bash
python Blackjack.py
```

### 4. Uno Simplifié

**Fichier :** `Uno.py`

**Règles :**
- Jeu contre l'ordinateur
- Chaque joueur reçoit 7 cartes au départ
- Une carte est retournée au centre de la table
- À votre tour, vous devez poser une carte qui a :
  - Soit la **même couleur** que la carte sur la table
  - Soit la **même valeur** que la carte sur la table
- Si vous ne pouvez pas jouer, vous piochez une carte
- Le premier joueur à ne plus avoir de cartes gagne la partie

**Fonctionnalités :**
- Affichage clair de vos cartes avec numérotation
- Vérification automatique des cartes jouables
- Impossible de jouer une carte invalide
- Gestion de la pioche vide
- Pause entre les tours pour suivre la partie

**Commande :**
```bash
python Uno.py
```

## Classes utilisées

### Classe `Carte`

**Fichier :** `Class/Cartes.py`

**Attributs :**
- `valeur` : La valeur de la carte (1, 2, 3, ..., Valet, Dame, Roi)
- `couleur` : La couleur de la carte (Pique, Coeur, Carreau, Trefle)
- `dico` : Dictionnaire statique pour convertir les valeurs en points

**Méthodes :**
- `__init__(valeur, couleur)` : Initialise une carte
- `tour_gagne()` : Retourne la valeur numérique de la carte pour les comparaisons
- `__str__()` : Retourne une représentation textuelle de la carte (ex: "Roi de Pique")

### Classe `Deck`

**Fichier :** `Class/Deck.py`

**Attributs :**
- `cartes` : Liste contenant toutes les cartes du paquet
- `couleurs` : Liste statique des 4 couleurs
- `valeurs` : Liste statique des 13 valeurs

**Méthodes :**
- `__init__()` : Crée un paquet de 52 cartes (4 couleurs × 13 valeurs)
- `melanger()` : Mélange aléatoirement les cartes du paquet

## Prérequis

- Python 3.x
- Module `random`

## Installation et lancement

1. Cloner le dépôt :
```bash
git clone https://github.com/Gigabitethernet-sys/jeux-cartes.git
cd jeux-cartes
```

2. Lancer un jeu :
```bash
# Pour la bataille
python Jeu_bataille.py

# Pour le Memory
python Jeu_carte2.py

# Pour le Blackjack
python Blackjack.py

# Pour le Uno
python Uno.py
```

## Utilisation de l'IA

L'IA a pu être sollicitée dans quelques parties de ce projet pour :

- Le débogage et la correction d'erreurs (indentation, erreur de frappeq...)
- La structuration des idées
- servir de guide pédagogique pour comprendre et apprendre certains concepts.

## Auteur
Elève de BTS SIO SISR - Première année  
2025-2026
