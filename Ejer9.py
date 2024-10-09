
#Ejercicio #9

import random

def adivinando():
    
    # Generar un número entre 1 y 100
    numero_aleatorio = random.randint(1, 100)
    intentos = 0
    adivinado = False

    print("¡Adivina el número entre 1 y 100!")

    while not adivinado:
        
        # While para solicitar el numero y validar que solo se puedan ingresar numeros enteros
        while True:
            try:
                intento = int(input("Ingresa tu intento: "))
                break
            except:
                print("Por favor, ingrese un número entero válido.")
        intentos += 1
        
        # Comparar los numeros e indicar si es mayor o meno
        if intento < numero_aleatorio:
            print("El número es mayor.")
        elif intento > numero_aleatorio:
            print("El número es menor.")
        else:
            adivinado = True
            print(f"¡Felicitaciones! Has adivinado el número en {intentos} intentos.")


#llamando a la funcion
adivinando()
