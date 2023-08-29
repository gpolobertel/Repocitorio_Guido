def fibonacci_digitos():
    digitos = int(input("Ingrese la cantidad de dígitos de la serie de Fibonacci: "))
    a, b = 0, 1
    contador = 0
    print("Serie de Fibonacci:")
    while contador < digitos:
        print(a, end=" ")
        a, b = b, a + b
        contador += 1
    print()

fibonacci_digitos()
