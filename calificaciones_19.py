import csv
import os

ARCHIVO_CSV = os.path.join(os.path.dirname(os.path.abspath(__file__)), "calificaciones(in).csv")
NOTA_APROBATORIA = 6.0


def leer_datos():
    alumnos = []
    with open(ARCHIVO_CSV, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for fila in reader:
            p1 = float(fila["Parcial1"])
            p2 = float(fila["Parcial2"])
            p3 = float(fila["Parcial3"])
            promedio = round((p1 + p2 + p3) / 3, 2)
            alumnos.append({
                "matricula": fila["Matricula"],
                "nombre": fila["Nombre"],
                "carrera": fila["Carrera"],
                "parcial1": p1,
                "parcial2": p2,
                "parcial3": p3,
                "promedio": promedio,
            })
    return alumnos


def mostrar_promedios(alumnos):
    print("=== PROMEDIOS INDIVIDUALES ===")
    for a in alumnos:
        print(f"{a['nombre']} ({a['carrera']}): {a['promedio']}")


def mostrar_mejor_peor(alumnos):
    mejor = max(alumnos, key=lambda a: a["promedio"])
    peor = min(alumnos, key=lambda a: a["promedio"])
    print(f"\n=== MEJOR PROMEDIO ===")
    print(f"{mejor['nombre']} - {mejor['promedio']}")
    print(f"\n=== PEOR PROMEDIO ===")
    print(f"{peor['nombre']} - {peor['promedio']}")


def mostrar_estadisticas(alumnos):
    promedio_general = round(sum(a["promedio"] for a in alumnos) / len(alumnos), 2)
    aprobados = sum(1 for a in alumnos if a["promedio"] >= NOTA_APROBATORIA)
    reprobados = len(alumnos) - aprobados
    print(f"\n=== ESTADISTICAS ===")
    print(f"Promedio general: {promedio_general}")
    print(f"Aprobados: {aprobados}")
    print(f"Reprobados: {reprobados}")


def mostrar_ranking(alumnos):
    ranking = sorted(alumnos, key=lambda a: a["promedio"], reverse=True)
    print("\n=== RANKING ===")
    for i, a in enumerate(ranking, 1):
        print(f"{i}. {a['nombre']} ({a['carrera']}) - {a['promedio']}")


def main():
    try:
        alumnos = leer_datos()
    except FileNotFoundError:
        print(f"Error: No se encontro '{ARCHIVO_CSV}'")
        return
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return

    if not alumnos:
        print("No hay datos de alumnos.")
        return

    mostrar_promedios(alumnos)
    mostrar_mejor_peor(alumnos)
    mostrar_estadisticas(alumnos)
    mostrar_ranking(alumnos)


if __name__ == "__main__":
    main()
