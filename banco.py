from cuenta import Cuenta
from database import DB

class Banco:
    def __init__(self):
        self.cuentas = {}
        self.db = DB()
        self.cuentas = {}
        print("Obteniendo cuentas de la DB...")
        self.obtener_cuentas_db()

    def crear_cuenta(self):
        # if id_cuenta not in self.cuentas:
        #     self.cuentas[id_cuenta] = Cuenta(id_cuenta)
        #     return True
        self.db.crear_cuenta()
        return False

    def obtener_cuenta(self, id_cuenta):
        return self.cuentas.get(id_cuenta, None)
    
    def obtener_cuentas(self):
        return self.cuentas
    
    def obtener_cuentas_db(self):
        cuentas = self.db.obtener_cuentas()
        for cuenta in cuentas:
            id = cuenta[0]
            saldo = cuenta[1]
            self.cuentas[id] = Cuenta(id, saldo)

    def transferir(self, id_origen, id_destino, monto):
        cuenta_origen = self.obtener_cuenta(id_origen)
        cuenta_destino = self.obtener_cuenta(id_destino)
        if cuenta_origen and cuenta_destino and cuenta_origen.retirar(monto):
            cuenta_destino.depositar(monto)
            return True
        return False
    
    def serializar_cuenta(self, cuenta):
        return {
            "id_cuenta": cuenta.id_cuenta,
            "saldo": cuenta.saldo
        }
    
    def serializar_cuentas(self):
        return [self.serializar_cuenta(cuenta) for cuenta in self.cuentas.values()]
    

# db = DB()
# db.obtener_cuentas()