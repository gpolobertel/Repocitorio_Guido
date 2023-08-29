import math as m

a=int(input('Ingrese a: '))
b=int(input('Ingrese b: '))
c=int(input('Ingrese c: '))
x1=(-b+m.sqrt(b**2-4*a*c))/(2*a)
x2=(-b-m.sqrt(b**2-4*a*c))/(2*a)
print('las soluciones son',x1,'y',x2)