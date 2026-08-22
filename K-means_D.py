import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
df = pd.read_csv(r"C:\Users\diego\Downloads\dataset_clientes.csv")

variables = [
    "Compras_Mensuales",
    "Gasto_Mensual_MXN",
    "Dias_Desde_Ultima_Compra"
]

datos = df[variables].dropna()

escalador = StandardScaler()
datos_estandarizados = escalador.fit_transform(datos)

modelo_kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

modelo_kmeans.fit(datos_estandarizados)

resultados = df.loc[
    datos.index,
    ["ID_Cliente"] + variables
].copy()

resultados["Cluster"] = modelo_kmeans.labels_

print("CLASIFICACIÓN DE LOS CLIENTES:")
print(resultados.to_string(index=False))

promedios = resultados.groupby("Cluster")[variables].mean().round(2)

print("\nPROMEDIOS POR CLÚSTER:")
print(promedios)

valores_k = range(1, 11)
inercias = []

for k in valores_k:
    modelo = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )
    
    modelo.fit(datos_estandarizados)
    inercias.append(modelo.inertia_)

plt.figure(figsize=(8, 5))
plt.plot(valores_k, inercias, marker="o", color="blue")

plt.title("Método del codo")
plt.xlabel("Número de clústeres (K)")
plt.ylabel("Inercia")
plt.xticks(valores_k)
plt.grid(True)

plt.show()