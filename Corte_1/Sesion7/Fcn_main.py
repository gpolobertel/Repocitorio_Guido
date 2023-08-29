import Fcn_ext
import Fun3

def app():
    print('Inicio')
    nombre = input('Ingrese su nombre: ')
    surname = input('Ingrese su apellido: ')
    print('--------------')
    Fcn_ext.matrix(nombre, surname)
    print('--------------')
    print(f'Ejecutado desde {__name__}')
    print('**************')
    a = int(input('Ingrese un número: '))
    b = int(input('ingrese otro número: '))
    Fun3.suma(a,b)
    print('**************')
    #s()

if __name__=="__main__":
    app()