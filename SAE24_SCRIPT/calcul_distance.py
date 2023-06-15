import math

# Coordonnées des microphones
microphones = [(0,0), (0,8), (8,8)]

# Dimensions de la grille de cases
grille_dim = 16

# Fonction pour calculer la distance entre deux points
def calculer_distance(x1, y1, x2, y2):
    return round(math.sqrt((x2 - x1)**2 + (y2 - y1)**2), 2)

# Ouverture du fichier texte en mode écriture
fichier_distances = open("distances_micro.txt", "w")

# Parcours de chaque case de la grille
for y in range(grille_dim):
    for x in range(grille_dim):
        # Parcours de chaque microphone
        for i, microphone in enumerate(microphones):
            distance = calculer_distance(x + 0, y + 0, microphone[0], microphone[1])
            # Écriture de la distance dans le fichier texte
            fichier_distances.write(f"Case ({x}, {y}) - Microphone {i+1}: {distance}\n")

# Fermeture du fichier texte
fichier_distances.close()
