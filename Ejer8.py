
#Ejercicio #8

def contar_vocales(palabra):
    vocales = "aeiouAEIOU"
    contador = 0
    
    for letra in palabra:
        if letra in vocales:
            contador += 1
    return contador

palabra = input("Ingrese una Palabra: ")

#llamamos la funcion y mostramos la cantidad de vocales
numero_vocales = contar_vocales(palabra)
print(f"El número total de vocales en la frase es: {numero_vocales}")
