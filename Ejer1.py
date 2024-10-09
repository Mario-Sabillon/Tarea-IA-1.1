
#ejercicio 1 

class rectangulo:
    def __init__(self, base, altura):
        self.base= float(base)
        self.altura= float(altura)
    
    def area(self):
        a = self.base * self.altura
        return a
    def perimetro(self):
        p = (self.base * 2) + (self.altura * 2)
        return p

rect = rectangulo(5, 3)
print ("El area del rectangulo es: ", rect.area())
print ("El perimtro del rectangulo es: ", rect.perimetro())

