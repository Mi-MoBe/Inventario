inventario = []
# funciones


def agregar_producto(inventario, nombre, precio, cantidad):
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }
    inventario.append(producto)


def mostrar_inventario(inventario):
    if not inventario:
        print("El inventario está vacío.")
    else:
        print("\n----INVENTARIO----")
        for p in inventario:
            print(
                f"Producto: {p['nombre']}, Precio: {p['precio']}, Cantidad: {p['cantidad']}")


def buscar_producto(inventario, nombre):
    for p in inventario:
        if p["nombre"] == nombre:
            return p
    return None


def actualizar_producto(inventario, nombre, precio=None, cantidad=None):
    producto = buscar_producto(inventario, nombre)
    if producto:
        if precio is not None:
            producto["precio"] = precio
        if cantidad is not None:
            producto["cantidad"] = cantidad
        print(f"Producto '{nombre}' actualizado.")
    else:
        print(f"Producto '{nombre}' no encontrado en el inventario.")


def eliminar_producto(inventario, nombre):
    producto = buscar_producto(inventario, nombre)
    if producto:
        inventario.remove(producto)
        print(f"Producto '{nombre}' eliminado del inventario.")
    else:
        print(f"Producto '{nombre}' no encontrado en el inventario.")


def calcular_valor_total(inventario):
    if not inventario:
        print("El inventario está vacío.")
        return
    total_unidades = sum(p["cantidad"] for p in inventario)
    valor_total = sum(p["precio"] * p["cantidad"] for p in inventario)

    producto_caro = max(inventario, key=lambda p: p["precio"])
    producto_stock = max(inventario, key=lambda p: p["cantidad"])

    print(f"\n----ESTADÍSTICAS----")
    print(f"Total de unidades en inventario: {total_unidades}")
    print(f"Valor total del inventario: {valor_total}")
    print(
        f"Producto más caro: {producto_caro['nombre']} (Precio: {producto_caro['precio']})")
    print(
        f"Producto con más stock: {producto_stock['nombre']} (Cantidad: {producto_stock['cantidad']})")



