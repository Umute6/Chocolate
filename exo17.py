symboles = ["♥", "♦", "♣", "♠"]
valeurs = ["As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

for carte in valeurs:
    for cartes in symboles:
        print(carte + " de " + cartes)