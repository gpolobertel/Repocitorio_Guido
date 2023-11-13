class Ciudadano:
    def __init__(self):
        self.nombre = ""
        self.cedula = ""
        self.edad = 0

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_nombre(self):
        return self.nombre

    def set_cedula(self, cedula):
        if len(cedula) >= 8 and len(cedula) <= 10:
            self.cedula = cedula
        else:
            print("La cédula debe tener entre 8 y 10 dígitos")

    def get_cedula(self):
        return self.cedula

    def set_edad(self, edad):
        if edad > 0:
            self.edad = edad
        else:
            print("La edad debe ser un número positivo mayor que cero")

    def get_edad(self):
        return self.edad

    def mostrar(self):
        print(f"Nombre: {self.nombre}\nEdad: {self.edad}\nCC: {self.cedula}")

    def esMayorDeEdad(self):
        return self.edad >= 18
print('-----------------menu--------------------')
# Programa principal
while True:
    ciudadano = Ciudadano()
    nombre = input("Ingrese el nombre del ciudadano: ")
    cedula = input("Ingrese la cédula del ciudadano: ")
    edad = input("Ingrese la edad del ciudadano: ")

    ciudadano.set_nombre(nombre)
    ciudadano.set_cedula(cedula)
    ciudadano.set_edad(int(edad))

    ciudadano.mostrar()
    print('\n----------------------------\n')
    if ciudadano.esMayorDeEdad():
        print("Es mayor de edad.")
    else:
        print("Es menor de edad.")

    salir = input("¿Desea salir? (Escriba 'salir' para salir): ")
    if salir.strip().lower() == 'salir':
        break
