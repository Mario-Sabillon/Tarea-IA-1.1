#Ejercicion #5

def primo(x):
    if x <= 1:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True


numero = None

# Solicitar del numero
while numero == None:   
    try:
        numero = int(input("Ingrese un numero entero: "))
    except:
        print("Ingreso un valor incorrecto")

#Validar si es o no primo
if primo(numero):
    print(f"El número {numero} es primo.")
else:
    print(f"El número {numero} no es primo.")
