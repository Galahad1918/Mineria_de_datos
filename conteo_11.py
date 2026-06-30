from collections import Counter
frutas = ["manzana", "pera", "manzana", "uva", "manzana"]
conteo = Counter(frutas)
print("Resultado del conteo:")
for elemento, cantidad in conteo.items():
    print(f"{elemento}: {cantidad}")
