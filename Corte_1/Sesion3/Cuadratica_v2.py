import math as m

a=int(input('Ingrese a: '))
b=int(input('Ingrese b: '))
c=int(input('Ingrese c: '))

raiz=b**2-4*a*c
if raiz>0:
    x1=(-b+m.sqrt(raiz))/(2*a)
    x2=(-b-m.sqrt(raiz))/(2*a)
    print('las soluciones son',x1,'y',x2)
else:
    raiz=m.fabs(raiz)
    x_r=-b/(2*a)
    x_i=(m.sqrt(raiz))/(2*a)
    print('las soluciones son:\n'\
        ,x_r,'+',x_i,'i\n'\
            ,x_r,'-',x_i,'i')
    