class Articulo:
    def __init__(self, nombre, precio):
        self._nombre = nombre
        self._precio = precio

    def setNombre(self, nombre):
        self._nombre = nombre

    def setPrecio(self, precio):
        self._precio = precio

    def getNombre(self):
        return self._nombre

    def getPrecio(self):
        return self._precio

class Articulo0IVA(Articulo):
    def __init__(self, nombre, precio):
        super().__init__(nombre, precio)
        self._iva = 0

    def calcularPrecioBruto(self):
        return self._precio * (1 + self._iva)

class Articulo5IVA(Articulo):
    def __init__(self, nombre, precio):
        super().__init__(nombre, precio)
        self._iva = 0.05

    def calcularPrecioBruto(self):
        return self._precio * (1 + self._iva)

class Articulo19IVA(Articulo):
    def __init__(self, nombre, precio):
        super().__init__(nombre, precio)
        self._iva = 0.19

    def calcularPrecioBruto(self):
        return self._precio * (1 + self._iva)

# Crear una función para el menú
def menu():
    while True:
        print("1. Crear un artículo con 0% de IVA")
        print("2. Crear un artículo con 5% de IVA")
        print("3. Crear un artículo con 19% de IVA")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            nombre = input("Ingrese el nombre del artículo: ")
            precio = float(input("Ingrese el precio del artículo: "))
            articulo = Articulo0IVA(nombre, precio)
            print(f"Has creado el artículo {articulo.getNombre()} con un precio bruto de {articulo.calcularPrecioBruto()}")
        elif opcion == "2":
            nombre = input("Ingrese el nombre del artículo: ")
            precio = float(input("Ingrese el precio del artículo: "))
            articulo = Articulo5IVA(nombre, precio)
            print(f"Has creado el artículo {articulo.getNombre()} con un precio bruto de {articulo.calcularPrecioBruto()}")
        elif opcion == "3":
            nombre = input("Ingrese el nombre del artículo: ")
            precio = float(input("Ingrese el precio del artículo: "))
            articulo = Articulo19IVA(nombre, precio)
            print(f"Has creado el artículo {articulo.getNombre()} con un precio bruto de {articulo.calcularPrecioBruto()}")
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

# Llamar a la función del menú solo si el script se ejecuta directamente
if __name__ == '__main__':
    menu()
