import math

def main():
    print("Calculadora de Vectores")
    print("-----------------------")

    # Solicitar coordenadas del origen
    x_origen = float(input("Ingrese la coordenada x del origen: "))
    y_origen = float(input("Ingrese la coordenada y del origen: "))
    
    # Solicitar coordenadas del fin
    x_fin = float(input("Ingrese la coordenada x del fin: "))
    y_fin = float(input("Ingrese la coordenada y del fin: "))
    
    # Calcular las diferencias en las coordenadas para obtener las componentes rectangulares
    delta_x = x_fin - x_origen
    delta_y = y_fin - y_origen
    
    # Calcular el módulo del vector
    modulo = math.sqrt(delta_x**2 + delta_y**2)
    
    # Imprimir resultados de manera bonita
    print("\nResultados")
    print("-----------------------")
    print(f"Componente x: {delta_x:.2f}")
    print(f"Componente y: {delta_y:.2f}")
    print(f"Módulo del vector: {modulo:.2f}")
    
if __name__ == "__main__":
    main()
