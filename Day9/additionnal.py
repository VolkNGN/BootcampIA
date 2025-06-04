import numpy as np

#Je veux Simuler des relevés de température (en degrés Celsius)
np.random.seed(0)  # pour reproductibilité
temperatures = np.random.normal(loc=45, scale=10, size=(10, 10))
print("Températures relevées :\n", temperatures)

#Je définis un seuil d'alerte
threshold = 50

# j'utilise un masque binaire afin de convertir mes données en integer.
mask = (temperatures > threshold).astype(int)
print("\nMasque binaire (1 si > 50°C, sinon 0) :\n", mask)

#Je veux compter le nombre de températures supérieurs au seuil fixé
count_above_threshold = np.sum(mask)
print(f"\nNombre de relevés supérieurs à {threshold}°C :", count_above_threshold)
