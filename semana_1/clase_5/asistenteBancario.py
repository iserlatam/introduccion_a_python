from semana_1.clase_5.modules.banco.cuentas import CuentaBancaria, CuentaAhorros, CuentaCorriente

# Crear instancias de las clases
cuenta1 = CuentaBancaria("Juan Perez", 1000)
cuenta2 = CuentaAhorros("Ana Gomez", 2000, 0.05)
cuenta3 = CuentaCorriente("Carlos Lopez", 500, 1500)

# # Operaciones con cuenta bancaria
# cuenta1.depositar(500)
# cuenta2.depositar(1000)

# cuenta1.retirar(200)
# cuenta1.mostrar_saldo()

# # Operaciones con cuenta de ahorros
# cuenta2.depositar(1000)
# cuenta2.aplicar_interes()
# cuenta2.mostrar_saldo()

# # Operaciones con cuenta corriente
cuenta3.retirar(1000)
cuenta3.retirar(600)
cuenta3.depositar(1200)
# cuenta3.mostrar_saldo()
