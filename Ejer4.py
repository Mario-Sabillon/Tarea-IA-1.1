
#Ejercicio 4|   

class Calculadora:
    def __init__(self, a, b):
        self.a = float (a)
        self.b = float (b)
    
    def dividir(self):
        if self.b != 0:
            print(f"El cociente de sus numeros es igual a: ", self.a / self.b)
        else:  
            print("Segun las normas matematicas, no podemos dividir entre 0")
            
    def multiplicar(self):
        print(f"El producto de su numeros es igual a: ", self.a * self.b)
        
    def sumar(self):
        print(f"La suma de su numeros es igual a: ", self.a + self.b)
        
    def restar(self):
        print(f"La resta de su numeros es igual a: ", self.a - self.b)
        

a = None
b = None

while b == None:   
    try:
        if a == None: 
            print("Ingrese su primer numero: ")
            a = float(input())
        print("Ingrese su segundo numero: ")
        b = float (input())
    except:
        print("Ingreso un valor incorrecto")
        
Operaciones = Calculadora(a,b)
Operaciones.dividir()
Operaciones.multiplicar()
Operaciones.sumar()
Operaciones.restar()
        
        