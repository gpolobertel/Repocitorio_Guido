def matrix(nombre,surname):
    print('Bienvenido a la matrix',nombre, surname)
    print(f'Ejecutado desde {__name__}')

def operacion():
    num1 = int(input('Ingrese un número: '))
    num2 = int(input('ingrese otro número: '))
    r = num1*num2
    print(r)

if __name__=="__main__":
    matrix('Falcao','Garcia')