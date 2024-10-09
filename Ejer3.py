#Ejercicio #3

class CuentaBancaria:
    def __init__(self, titular):
        self.titular = str (titular)
        self.saldo = float(0.0)

    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f"+ + Depósito Realizado en la cuenta de {self.titular} por la cantidad de {cantidad}")

    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"- - Retiro Realizado en la cuenta de {self.titular} por la cantidad de {cantidad}")
        else:
            print(f"*******************Estimado {self.titular} Sus fondos insuficientes para realizar el retiro.***********")

    def mostrar_saldo(self):
        print(f"= = = = Su Saldo actual es: {self.saldo}")


cuenta = CuentaBancaria("Mario Sabillon")

# Depósitos, Retiros y mostar Saldo
cuenta.depositar(10000)
cuenta.mostrar_saldo()
cuenta.retirar(5000)
cuenta.retirar(6000) #para generar error de fondos
cuenta.mostrar_saldo()
cuenta.retirar(1600)
cuenta.mostrar_saldo()
cuenta.depositar(10000)
cuenta.mostrar_saldo()
