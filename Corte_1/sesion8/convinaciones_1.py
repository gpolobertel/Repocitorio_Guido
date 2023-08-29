def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def combinaciones_binomiales(n, r):
    comb_binomial = factorial(n) / (factorial(r) * factorial(n-r))
    return comb_binomial

n = int(input("Ingrese el valor de n: "))
r = int(input("Ingrese el valor de r: "))

num_combinaciones = combinaciones_binomiales(n, r)
print("El número de combinaciones binomiales es:", num_combinaciones)
