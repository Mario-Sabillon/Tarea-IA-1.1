#Ejercicio #7

while True:
    try:
        num = int(input("Ingrese un número entero: "))
        break
    except:
        # Mensaje si no ingresa un número entero
        print("Valor Ingresador incorrecto!")


print(f"\n Tabla de multiplicar del {num}: ")
for i in range(1, 11):
    resultado = num * i
    print(f"{num} x {i} = {resultado}")
