import pandas as pd
# Leer el archivo
datos = pd.read_csv("estudiantes.csv")

variables = ["Asistencia", "Tareas", "Examen"]

for variable in variables:
    print("\nVariable:", variable)
    print("Media:", datos[variable].mean())
    print("Mediana:", datos[variable].median())
    print("Moda:", datos[variable].mode()[0])