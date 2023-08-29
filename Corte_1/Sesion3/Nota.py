nota=float(input('Ingrese su nota: '))

#if (nota>=0 and nota<=5):
if(0<=nota<=5):
    if nota>=3:
        print('Aprobó')
    else:
        print('Reprobó')
else:
    print('La nota ingresada es invalida')