def factorial(n):
    if n != 0:
        return n * factorial(n - 1)
    else:
        return 1


numero = float(input("Ingresa el numero para calcular el factorial: "))

print("Factorial de", numero, "es", factorial(numero))
