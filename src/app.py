from servicios import *
from archivos import *
import csv

inventario = []
# -------------------------
# MENÚ PRINCIPAL
# -------------------------

while True:
    print("\n--- MENÚ ---")
    print("1. Agregar")
    print("2. Mostrar")
    print("3. Buscar")
    print("4. Actualizar")
    print("5. Eliminar")
    print("6. Estadísticas")
    print("7. Guardar CSV")
    print("8. Cargar CSV")
    print("9. Salir")

    try:
        opcion = int(input("Elige una opción: "))
    except ValueError:
        print("Entrada inválida.")
        continue

    if opcion == 1:
        nombre = input("Nombre: ").lower()
        try:
            precio = float(input("Precio: "))
            cantidad = int(input("Cantidad: "))
            if precio < 0 or cantidad < 0:
                print("No se permiten valores negativos.")
                continue
        except ValueError:
            print("Datos inválidos.")
            continue
        agregar_producto(inventario, nombre, precio, cantidad)

    elif opcion == 2:
        mostrar_inventario(inventario)

    elif opcion == 3:
        nombre = input("Buscar producto: ").lower()
        producto = buscar_producto(inventario, nombre)
        if producto:
            print(
                f"Producto: {producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}")
        else:
            print("No encontrado.")

    elif opcion == 4:
        nombre = input("Producto a actualizar: ").lower()
        try:
            precio = input("Nuevo precio (enter para omitir): ")
            cantidad = input("Nueva cantidad (enter para omitir): ")

            precio = float(precio) if precio else None
            cantidad = int(cantidad) if cantidad else None

            actualizar_producto(inventario, nombre, precio, cantidad)
        except ValueError:
            print("Datos inválidos.")

    elif opcion == 5:
        nombre = input("Producto a eliminar: ").lower()
        eliminar_producto(inventario, nombre)

    elif opcion == 6:
        calcular_valor_total(inventario)

    elif opcion == 7:
        ruta = input("Ruta del archivo: ")
        guardar_csv(inventario, ruta)

    elif opcion == 8:
        ruta = input("Ruta del archivo: ")
        cargar_csv(ruta)

    elif opcion == 9:
        print("Saliendo...")
        break

    else:
        print("Opción inválida.")
