class Ciudadano:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Medico(Ciudadano):
    def __init__(self, nombre, edad, especialidad, hospital):
        super().__init__(nombre, edad)
        self.especialidad = especialidad
        self.hospital = hospital

    def diagnosticar(self, enfermedad):
        return f"El médico {self.nombre} ha diagnosticado {enfermedad}"

class Profesor(Ciudadano):
    def __init__(self, nombre, edad, asignatura, colegio):
        super().__init__(nombre, edad)
        self.asignatura = asignatura
        self.colegio = colegio

    def enseñar(self, tema):
        return f"El profesor {self.nombre} está enseñando {tema}"

class Ingeniero(Ciudadano):
    def __init__(self, nombre, edad, campo, empresa):
        super().__init__(nombre, edad)
        self.campo = campo
        self.empresa = empresa

    def diseñar(self, proyecto):
        return f"El ingeniero {self.nombre} está diseñando {proyecto}"

    # Sobrecarga del método diagnosticar para la clase Ingeniero
    def diagnosticar(self, problema):
        return f"El ingeniero {self.nombre} ha diagnosticado el problema {problema}"

# Crear una función para el menú
def menu():
    while True:
        print("1. Crear un médico")
        print("2. Crear un profesor")
        print("3. Crear un ingeniero")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            nombre = input("Ingrese el nombre del médico: ")
            edad = input("Ingrese la edad del médico: ")
            especialidad = input("Ingrese la especialidad del médico: ")
            hospital = input("Ingrese el hospital del médico: ")
            medico = Medico(nombre, edad, especialidad, hospital)
            print(f"Has creado al médico {medico.nombre}, de {medico.edad} años, especializado en {medico.especialidad}, que trabaja en el hospital {medico.hospital}.")
            enfermedad = input("Ingrese una enfermedad para que el médico la diagnostique: ")
            print(medico.diagnosticar(enfermedad))
        elif opcion == "2":
            nombre = input("Ingrese el nombre del profesor: ")
            edad = input("Ingrese la edad del profesor: ")
            asignatura = input("Ingrese la asignatura del profesor: ")
            colegio = input("Ingrese el colegio del profesor: ")
            profesor = Profesor(nombre, edad, asignatura, colegio)
            print(f"Has creado al profesor {profesor.nombre}, de {profesor.edad} años, que enseña {profesor.asignatura} en el colegio {profesor.colegio}.")
            tema = input("Ingrese un tema para que el profesor lo enseñe: ")
            print(profesor.enseñar(tema))
        elif opcion == "3":
            nombre = input("Ingrese el nombre del ingeniero: ")
            edad = input("Ingrese la edad del ingeniero: ")
            campo = input("Ingrese el campo del ingeniero: ")
            empresa = input("Ingrese la empresa del ingeniero: ")
            ingeniero = Ingeniero(nombre, edad, campo, empresa)
            print(f"Has creado al ingeniero {ingeniero.nombre}, de {ingeniero.edad} años, que trabaja en el campo de {ingeniero.campo} para la empresa {ingeniero.empresa}.")
            proyecto = input("Ingrese un proyecto para que el ingeniero lo diseñe: ")
            print(ingeniero.diseñar(proyecto))
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

# Llamar a la función del menú solo si el script se ejecuta directamente
if __name__ == '__main__':
    menu()
