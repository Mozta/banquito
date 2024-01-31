class Cuenta:
    def __init__(self, id_cuenta, saldo=0):
        self.id_cuenta = id_cuenta
        self.saldo = saldo

    def depositar(self, monto):
        self.saldo += monto

    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
            return True
        return False

    def transferir(self, cuenta_destino, monto):
        if self.retirar(monto):
            cuenta_destino.depositar(monto)
            return True
        return False
    
    def __str__(self):
        return f'Cuenta: {self.id_cuenta} Saldo: {self.saldo}'
        
    
