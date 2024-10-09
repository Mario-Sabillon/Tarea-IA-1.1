
#Ejercicio #10

import random
import string

def generar(tamano):
    if tamano < 8:
        print("La longitud mínima de la contraseña debe ser de 8 caracteres.")
        return None

    caracteres = string.ascii_letters + string.digits + string.punctuation #definimos los valores de caracteres permitidos
    contrasena = ''.join(random.choice(caracteres) for i in range(tamano)) #generamos la contraseña
    return contrasena

# Solicitar al usuario que ingrese el tamaño de la contraseña
while True:
    try:
        tamano = int(input("Ingrese el numero de caracteres que desea para su contraseña (mínimo 8 caracteres): "))
        if tamano < 8:
            print("La longitud mínima de la contraseña debe ser de 8 caracteres.")
        else:
            break
    except:
        print("Por favor, ingrese un número válido.")

# Generar y mostrar la contraseña
contrasena = generar(tamano)
if contrasena:
    print(f"La contraseña generada es: {contrasena}")

