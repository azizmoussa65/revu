import random

def generate_data(n):
    data = []
    for _ in range(n):
        data.append(random.randint(1, 100))
    return data

# Utilisation de la fonction pour générer 10 nombres aléatoires
data = generate_data(10)
print(data)