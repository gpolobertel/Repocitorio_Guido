# Funcion sin parametros y sin retorno

def suma(num1,num2):
    r = num1+num2
    print(r)
    print(f'Ejecutado desde {__name__}')


if __name__=="__main__":
    print('Inicio de prueba')

    suma(10,15)

    print('Fin del prueba')
