r=float(input('Ingrese el radio: '))
V=(4/3)*(3.1416)*(r**3)
V=V*1000
print('El volumen de un recipiente de radio '\
    ,r,'metros es ',round(V,2), 'Litros')