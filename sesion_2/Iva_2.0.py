def calcular_total(parqueo_minutos):
    tarifa_por_minuto = 139
    subtotal = parqueo_minutos * tarifa_por_minuto
    iva = subtotal * 0.19
    total_sin_iva = subtotal + iva
    total_con_iva = round(total_sin_iva / 50) * 50  # Aproximar al siguiente múltiplo de $50
    return total_con_iva

def main():
    print("=== Bienvenido al Estacionamiento ===")
    parqueo_minutos = int(input("Ingrese el tiempo de parqueo en minutos: "))
    
    total_con_iva = calcular_total(parqueo_minutos)
    
    print("\n--- Tiquet de Precio ---")
    print(f"Tiempo de parqueo: {parqueo_minutos} minutos")
    print(f"Subtotal: ${parqueo_minutos * 139:.2f}")
    print(f"IVA (19%): ${total_con_iva * 0.19:.2f}")
    print(f"Total a pagar: ${total_con_iva:.2f}")

if __name__ == "__main__":
    main()
