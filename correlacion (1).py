import pandas as pd
import matplotlib.pyplot as plt
dt = pd.read_csv("estudiantes.csv")

correlacion = dt["Asistencia"].corr(dt["Calificacion_Final"])
print("correlacion entre asistencia y calificacion final:", correlacion)

correlacion = dt["Examen"].corr(dt["Calificacion_Final"])
print("correlacion entre examen y calificacion final:", correlacion)

correlacion = dt["Horas_Estudio"].corr(dt["Calificacion_Final"])
print("correlacion entre horas de estudio y calificacion final:", correlacion)

correlacion = dt["Tareas"].corr(dt["Calificacion_Final"])
print("correlacion entre tareas y calificacion final:", correlacion)

correlacion = dt["Edad"].corr(dt["Calificacion_Final"])
print("correlacion entre Edad y calificacion final:", correlacion)
 
plt.scatter(dt["Asistencia"], dt["Calificacion_Final"])
plt.xlabel("Asistencia")
plt.ylabel("Calificación final")
plt.title("asistencia vs Calificación final")
plt.show()

plt.scatter(dt["Examen"], dt["Calificacion_Final"])
plt.xlabel("Examen")
plt.ylabel("Calificación final")
plt.title("Examen vs Calificación final")
plt.show()

plt.scatter(dt["Horas_Estudio"], dt["Calificacion_Final"])
plt.xlabel("Horas_Estudio")
plt.ylabel("Calificación final")
plt.title("Horas_Estudio vs Calificación final")
plt.show()

plt.scatter(dt["Tareas"], dt["Calificacion_Final"])
plt.xlabel("Tareas")
plt.ylabel("Calificación final")
plt.title("Tareas vs Calificación final")
plt.show()

plt.scatter(dt["Edad"], dt["Calificacion_Final"])
plt.xlabel("Edad")
plt.ylabel("Calificación final")
plt.title("Edad vs Calificación final")
plt.show()