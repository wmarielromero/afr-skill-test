class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, monto):
        self.saldo += monto

    def retirar(self, monto):
        if self.saldo >= monto:
            self.saldo -= monto
        else:
            print("Saldo insuficiente")

    def obtener_saldo(self):
        return self.saldo
    
# No modificar el siguiente bloque
cuenta = CuentaBancaria("Ana", 100)
cuenta.depositar(50)
cuenta.retirar(200)
print(cuenta.obtener_saldo())