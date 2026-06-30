# Escribir una función que reciba un número entero positivo y devuelva su factorial.
def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado
numero = int(input("Ingresa un número entero positivo: "))
print("El factorial es:", factorial(numero))
