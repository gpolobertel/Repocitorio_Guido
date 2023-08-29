def producto_sumas():
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    resultado = 0
    for _ in range(abs(num2)):
        resultado += abs(num1)
    if (num1 < 0 and num2 > 0) or (num1 > 0 and num2 < 0):
        resultado = -resultado
    print(f"El producto de {num1} y {num2} es: {resultado}")

producto_sumas()
