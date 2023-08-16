def es_vocal(letra):
    vocales = "aeiouAEIOU"
    return letra in vocales

def main():
    print("Bienvenido al verificador de vocales y consonantes!")
    letra = input("Ingresa una letra del abecedario: ")

    if len(letra) == 1 and letra.isalpha():
        if es_vocal(letra):
            print(f"{letra} es una vocal.")
        else:
            print(f"{letra} es una consonante.")
    else:
        print("Ingresa una única letra válida del abecedario.")

if __name__ == "__main__":
    main()
