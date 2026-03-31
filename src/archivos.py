import csv


def guardar_csv(inventario, ruta):
    import os
    try:
        print("Guardando en:", os.path.abspath(ruta))

        with open(ruta, "w") as f:
            f.write("nombre,precio,cantidad\n")
            for p in inventario:
                f.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")

        print(f"Inventario guardado en {ruta}")
    except Exception as e:
        print(f"Error al guardar el inventario: {e}")


def cargar_csv(ruta):
    inventario = []
    try:
        with open(ruta, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                inventario.append({
                    "nombre": row["nombre"],
                    "precio": float(row["precio"]),
                    "cantidad": int(row["cantidad"])
                })
        print("Inventario cargado.")
    except FileNotFoundError:
        print("Error: No se encontró el archivo.")
    except ValueError as e:
        print(f"Error de formato en los datos: {e}")
    except Exception as e:
        print(f"Error al cargar: {e}")
    return inventario
