n = int(input('ingrese la cantidad de primos solicitada: '))
con = 0  # Comenzamos con 0 primos encontrados
x = 2
numero = ''

while con < n:
    es_primo = True
    for i in range(2, x):
        if x % i == 0:
            es_primo = False
            break

    if es_primo:
        numero += str(f'{x} ')
        con += 1

    x += 1

print(f'{numero}')
