class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = 0

    def obtener_info(self):
        return f"Nombre: {self.nombre}, Precio: {self.precio}, Cantidad: {self.cantidad}"

    def restar_cantidad(self):
        if self.cantidad > 0:
            self.cantidad -= 1

    def verificar_disponibilidad(self):
        return self.cantidad > 0


class Snack(Producto):
    def __init__(self, nombre, precio, tipo):
        super().__init__(nombre, precio)
        self.tipo = tipo

    def obtener_info(self):
        return super().obtener_info() + f", Tipo: {self.tipo}"


class Bebida(Producto):
    def __init__(self, nombre, precio, tamaño):
        super().__init__(nombre, precio)
        self.tamaño = tamaño

    def obtener_info(self):
        return super().obtener_info() + f", Tamaño: {self.tamaño}"


class MaquinaDispensadora:
    def __init__(self):
        self.productos = []
        self.total_ventas = 0

    def agregar_producto(self, producto):
        cantidad = int(input("Ingrese la cantidad inicial del producto: "))
        producto.cantidad = cantidad
        self.productos.append(producto)

    def realizar_venta(self, producto):
        if producto.verificar_disponibilidad():
            producto.restar_cantidad()
            self.total_ventas += producto.precio
            return True
        else:
            return False

    def obtener_total_ventas(self):
        return self.total_ventas

# Crear una máquina dispensadora
maquina = MaquinaDispensadora()

# Menú interactivo
while True:
    print('\n-------------Maquina dispensadora-------------\n')
    print("1. Agregar un producto")
    print("2. Realizar una venta")
    print("3. Ver total de ventas")
    print("4. Ver todos los productos")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")
    print('\n---------------------------------------\n')
    if opcion == "1":
        tipo = input("Ingrese el tipo de producto (snack o bebida): ")
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        if tipo.lower() == "snack":
            tipo_snack = input("Ingrese el tipo de snack (dulce o salado): ")
            producto = Snack(nombre, precio, tipo_snack)
        elif tipo.lower() == "bebida":
            tamaño = input("Ingrese el tamaño de la bebida (pequeño o grande): ")
            producto = Bebida(nombre, precio, tamaño)
        else:
            print("Tipo de producto no válido. Intente de nuevo.")
            continue
        maquina.agregar_producto(producto)
        print(f"Producto agregado: {producto.obtener_info()}")
    elif opcion == "2":
        nombre = input("Ingrese el nombre del producto que desea comprar: ")
        producto = next((p for p in maquina.productos if p.nombre == nombre), None)
        if producto is not None and maquina.realizar_venta(producto):
            print(f"Venta realizada: {producto.obtener_info()}")
        else:
            print("Venta no realizada. El producto no está disponible.")
    elif opcion == "3":
        print(f"Total de ventas: {maquina.obtener_total_ventas()}")
    elif opcion == "4":
        for producto in maquina.productos:
            print(producto.obtener_info())
    elif opcion == "5":
        break
    else:
        print("Opción no válida. Intente de nuevo.")
