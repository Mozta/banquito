import threading

class Cliente:
    def __init__(self, nombre, apellido, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni

    def __str__(self):
        return f'Nombre: {self.nombre} Apellido: {self.apellido} DNI: {self.dni}'
    
class Cuenta:
    def __init__(self, cliente, saldo):
        self.cliente = cliente
        self.saldo = saldo

    def __str__(self):
        return f'Cliente: {self.cliente} Saldo: {self.saldo}'

    def mostrar_saldo(self):
        return f'Saldo: {self.saldo}'
    
class Retiro:
    def __init__(self, cuenta, monto):
        self.cuenta = cuenta
        self.monto = monto

    def __str__(self):
        return f'Cuenta: {self.cuenta} Monto: {self.monto}'
    
class Deposito:
    def __init__(self, cuenta, monto):
        self.cuenta = cuenta
        self.monto = monto

    def __str__(self):
        return f'Cuenta: {self.cuenta} Monto: {self.monto}'
    
class Transferencia:
    def __init__(self, cuenta_origen, cuenta_destino, monto):
        self.cuenta_origen = cuenta_origen
        self.cuenta_destino = cuenta_destino
        self.monto = monto

    def __str__(self):
        return f'Cuenta origen: {self.cuenta_origen} Cuenta destino: {self.cuenta_destino} Monto: {self.monto}'

    def transferir(self):
        self.cuenta_origen.saldo -= self.monto
        self.cuenta_destino.saldo += self.monto
        return f'Transferencia realizada. Saldo cuenta origen: {self.cuenta_origen.saldo} Saldo cuenta destino: {self.cuenta_destino.saldo}'
    
class Historial:
    def __init__(self):
        self.historial = []

    def agregar(self, movimiento):
        self.historial.append(movimiento)

    def __str__(self):
        return f'{self.historial}'
    

def realizar_transaccion(cuenta, monto):
    # Aquí se podría hacer un retiro, depósito o transferencia
    # Por ejemplo, un retiro:
    if cuenta.saldo >= monto:
        cuenta.saldo -= monto
        print(f"Retiro exitoso. Saldo restante: {cuenta.saldo}")
    else:
        print("Fondos insuficientes.")



# Crear cliente y cuenta
cliente = Cliente("Nombre", "Apellido", "DNI")
cuenta = Cuenta(cliente, 1000)  # Saldo inicial de 1000

# Crear hilos para simular transacciones concurrentes
hilos = []
for _ in range(10):
    hilo = threading.Thread(target=realizar_transaccion, args=(cuenta, 100))
    hilos.append(hilo)
    hilo.start()

# Esperar a que todos los hilos terminen
for hilo in hilos:
    hilo.join()

print(f"Saldo final: {cuenta.saldo}")