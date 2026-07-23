import pandas as pd
import matplotlib.pyplot as plt
 
df = pd.read_csv("estudiantes.csv")
 
plt.scatter(df["Horas_Estudio"], df["Calificacion_Final"])
plt.xlabel("Horas de estudio")
plt.ylabel("Calificación final")
plt.title("Horas de estudio vs Calificación final")
plt.show()
 