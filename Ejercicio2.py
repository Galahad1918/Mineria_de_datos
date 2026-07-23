import pandas as pd
datos = pd.read_csv("estudiantes.csv")
variables = [
    "Asistencia",
    "Tareas",
    "Examen",
    "Calificacion_Final",
    "Horas_Estudio"
]
for variable in variables:
    print("\nVariable:", variable)

    rango=datos[variable].max()-datos[variable].min()
    varianza=datos[variable].var()
    desviacion=datos[variable].std()

    print("Rango:", rango)
    print("Varianza:", varianza)
    print("Desviación estándar:", desviacion)