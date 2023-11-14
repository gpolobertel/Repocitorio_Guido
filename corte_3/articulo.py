class Articulos:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Articulo0IVA(Articulos):
    def __init__(self, nombre, precio):
        super().__init__(nombre, precio)
        self.iva = 0

    def calcular_precio_bruto(self):
        return self.precio * (1 + self.iva)

class Articulo5IVA(Articulos):
    def __init__(self, nombre, precio):
        super().__init__(nombre, precio)
        self.iva = 0.05

    def calcular_precio_bruto(self):
        return self.precio * (1 + self.iva)

class Articulo19IVA(Articulos):
    def __init__(self, nombre, precio):
        super().__init__(nombre, precio)
        self.iva = 0.19

    def calcular_precio_bruto(self):
        return self.precio * (1 + self.iva)

def menu():
    while True:
        print('\n---------------menu-------------\n')
        print('1. Artículo con 0% IVA')
        print('2. Artículo con 5% IVA')
        print('3. Artículo con 19% IVA')
        print("4. Salir")
        opcion = input('Seleccione una opción: ')
        print('\n--------------------------------------\n')
        if opcion == '4':
            break
        nombre = input('Ingrese el nombre del artículo: ')
        precio = float(input("Ingrese el precio del artículo: "))
        if opcion == "1":
            articulo = Articulo0IVA(nombre, precio)
        elif opcion == "2":
            articulo = Articulo5IVA(nombre, precio)
        elif opcion == "3":
            articulo = Articulo19IVA(nombre, precio)
        print(f'\nEl precio bruto del {articulo.nombre} es {articulo.calcular_precio_bruto()} y el valor del IVA es {articulo.precio * articulo.iva}')

menu()
