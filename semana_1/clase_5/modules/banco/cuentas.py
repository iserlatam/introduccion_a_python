# Clase principal de tipo cuenta
class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Depósito de {cantidad} realizado. Nuevo saldo: {self.saldo}")
        else:
            print("Cantidad de depósito no válida")

    def retirar(self, cantidad):
        if 0 < cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Retiro de {cantidad} realizado. Nuevo saldo: {self.saldo}")
        else:
            print("Cantidad de retiro no válida o saldo insuficiente")

    def mostrar_saldo(self):
        print(f"El saldo de la cuenta es: {self.saldo}")

# Cuenta de ahorros -> Hereda de CuentaBancaria
class CuentaAhorros(CuentaBancaria):
    def __init__(self, titular, saldo=0, tasa_interes=0.01):
        super().__init__(titular, saldo)
        self.tasa_interes = tasa_interes

    def aplicar_interes(self):
        interes = self.saldo * self.tasa_interes
        self.depositar(interes)
        print(f"Intereses aplicados: {interes}. Nuevo saldo: {self.saldo}")

# Cuenta corriente -> Hereda de CuentaBancaria
class CuentaCorriente(CuentaBancaria):
    def __init__(self, titular, saldo=0, limite_descubierto=500):
        super().__init__(titular, saldo)
        self.limite_descubierto = limite_descubierto

    def retirar(self, cantidad):
        if 0 < cantidad <= self.saldo + self.limite_descubierto:
            self.saldo -= cantidad
            print(f"Retiro de {cantidad} realizado. Nuevo saldo: {self.saldo}")
        else:
            print("Cantidad de retiro no válida o saldo insuficiente")
