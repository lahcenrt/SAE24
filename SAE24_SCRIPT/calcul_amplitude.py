import math

# Coordonnées des microphones
microphones = [(0, 0), (0, 8), (8, 8)]

# Dimensions de la grille de cases
grille_dim = 16

# Constante d'amplitude
k = 1.0

# Fonction pour calculer la distance entre deux points
def calculer_distance(x1, y1, x2, y2):
    return round(math.sqrt((x2 - x1)**2 + (y2 - y1)**2), 2)

# Parcours de chaque microphone
for i, microphone in enumerate(microphones):
    # Ouverture du fichier texte en mode écriture
    fichier_amplitudes = open(f"amplitudes_micro_{i+1}.txt", "w")

    # Parcours de chaque case de la grille
    for y in range(grille_dim):
        for x in range(grille_dim):
            distance = calculer_distance(x, y, microphone[0], microphone[1])
            
            if distance == 0:
                amplitude = 0
            else:
                amplitude = k / (distance**2)
            
            # Écriture de l'amplitude dans le fichier texte
            fichier_amplitudes.write(f"Case ({x}, {y}): {amplitude}\n")

    # Fermeture du fichier texte
    fichier_amplitudes.close()
