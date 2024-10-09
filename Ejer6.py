#Ejercicio #6


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=", " if _ < n - 1 else "\n")
        a, b = b, a + b

#ingrese el valor 
while True:
    try:
        n = int(input("Ingrese el número de términos: "))
        if n <= 0:
            print("Por favor, ingrese un número entero positivo.")
        else:
            break
    except:
        print("Ingreso un valor incorrecto.")

# Llamar a la función para mostrar la secuencia
print("Secuencia de Fibonacci:")
fibonacci(n)
