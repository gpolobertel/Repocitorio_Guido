def calcular_divisores(numero):
    divisores = []
    for i in range(1, numero):
        if numero % i == 0:
            divisores.append(i)
    return divisores

def es_numero_perfecto(numero):
    divisores = calcular_divisores(numero)
    suma_divisores = sum(divisores)
    return suma_divisores == numero

def main():
    print("¡Bienvenido al buscador de números perfectos!")
    cantidad_perfectos = int(input("Ingrese la cantidad de números perfectos que desea encontrar (máximo 10): "))
    
    if cantidad_perfectos > 10:
        print("Lo siento, solo puedo encontrar hasta 10 números perfectos.")
        return
    
    encontrados = 0
    numero = 2  # Comenzamos desde 2 ya que 1 no se considera un número perfecto
    
    while encontrados < cantidad_perfectos:
        if es_numero_perfecto(numero):
            print(f"Número perfecto encontrado: {numero}")
            encontrados += 1
        numero += 1
    
    print("Búsqueda de números perfectos completada. ¡Hasta luego!")

if __name__ == "__main__":
    main()
