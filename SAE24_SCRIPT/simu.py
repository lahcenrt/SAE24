import random
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

# Sélection aléatoire d'une case de la grille
x = random.randint(0, grille_dim - 1)
y = random.randint(0, grille_dim - 1)

# Chemin d'accès absolu du fichier texte
chemin_fichier = "/home/rick/Desktop/SAE24/simu.txt"

# Écriture de la case sélectionnée dans le fichier texte
with open(chemin_fichier, "w") as fichier_amplitudes:
    fichier_amplitudes.write(f"Case sélectionnée : ({x}, {y})\n\n")

    # Parcours de chaque microphone
    for i, microphone in enumerate(microphones):
        distance = calculer_distance(x, y, microphone[0], microphone[1])
        
        if distance == 0:
            amplitude = 0
        else:
            amplitude = k / (distance**2)
        
        # Écriture de l'amplitude et de la case correspondante dans le fichier texte
        fichier_amplitudes.write(f"Microphone {i+1}: Amplitude = {amplitude}, Case = ({microphone[0]}, {microphone[1]})\n")

print("Le fichier amplitudes_case_aleatoire.txt a été créé avec succès.")
