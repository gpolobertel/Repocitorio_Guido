def divisores_numero():
    numero = int(input("Ingrese un número: "))
    if numero == 0:
        print("Ningún número es divisible entre cero")
    else:
        print(f"Divisores de {numero}:")
        for i in range(1, abs(numero) + 1):
            if numero % i == 0:
                print(i)

divisores_numero()