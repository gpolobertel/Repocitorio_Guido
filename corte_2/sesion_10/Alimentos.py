# Función para leer el archivo Alimentos.txt y organizar los productos según el IVA
def cargar_productos():
    productos = {}
    with open("Alimentos.txt", "r") as archivo:
        for linea in archivo:
            nombre, iva = linea.strip().split(",")
            productos[nombre] = float(iva)
    return productos

# Función para calcular el valor base y el valor del IVA de un producto
def calcular_valor_producto(productos, producto, valor_neto):
    if producto in productos:
        iva = productos[producto]
        valor_base = valor_neto / (1 + iva)
        valor_iva = valor_neto - valor_base
        return valor_base, valor_iva
    else:
        return None

# Cargar los productos desde el archivo
productos = cargar_productos()

while True:
    producto = input("Ingrese un producto (o escriba 'salir' para salir): ")
    
    if producto.lower() == "salir":
        break
    
    valor_neto = float(input("Ingrese el valor neto del producto: "))
    
    resultado = calcular_valor_producto(productos, producto, valor_neto)
    
    if resultado:
        valor_base, valor_iva = resultado
        print(f"Valor Base: {valor_base:.2f}")
        print(f"Valor del IVA: {valor_iva:.2f}")
    else:
        print("Producto no encontrado en la lista.")
