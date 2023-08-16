def es_triangulo(a, b, c):
    return a + b > c and a + c > b and b + c > a

def tipo_triangulo(a, b, c):
    if a == b == c:
        return "Equilátero"
    elif a == b or a == c or b == c:
        return "Isósceles"
    else:
        return "Escaleno"

def main():
    print("Bienvenido al programa de verificación de triángulos")
    
    while True:
        opciones = ["1. Verificar triángulo", "2. Salir"]
        print("\n".join(opciones))
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            a = float(input("Ingresa la longitud del primer lado: "))
            b = float(input("Ingresa la longitud del segundo lado: "))
            c = float(input("Ingresa la longitud del tercer lado: "))
            
            if es_triangulo(a, b, c):
                tipo = tipo_triangulo(a, b, c)
                print(f"¡Se puede formar un triángulo {tipo}!")
            else:
                print("No es posible formar un triángulo con las longitudes dadas.")
        elif opcion == "2":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elige una opción correcta.")

if __name__ == "__main__":
    main()
