from flask import Flask, request, jsonify
from banco import Banco

app = Flask(__name__)
banco = Banco()

@app.route('/crear_cuenta/<int:id_cuenta>', methods=['POST'])
def crear_cuenta(id_cuenta):
    if banco.crear_cuenta(id_cuenta):
        return jsonify({"mensaje": "Cuenta creada exitosamente"}), 201
    else:
        return jsonify({"mensaje": "La cuenta ya existe"}), 400
    
@app.route('/cuentas/', methods=['GET'])
def obtener_cuentas():
    return jsonify(banco.serializar_cuentas()), 200
    
@app.route('/', methods=['GET'])
def home():
    return jsonify({"mensaje": "Bienvenido al banco"}), 200

@app.route('/depositar/<int:id_cuenta>', methods=['POST'])
def depositar(id_cuenta):
    monto = request.json['monto']
    cuenta = banco.obtener_cuenta(id_cuenta)
    if cuenta:
        cuenta.depositar(monto)
        return jsonify({"saldo": cuenta.saldo}), 200
    return jsonify({"mensaje": "Cuenta no encontrada"}), 404

@app.route('/retirar/<int:id_cuenta>', methods=['POST'])
def retirar(id_cuenta):
    monto = request.json['monto']
    cuenta = banco.obtener_cuenta(id_cuenta)
    if cuenta:
        if cuenta.retirar(monto):
            return jsonify({"saldo": cuenta.saldo}), 200
        return jsonify({"mensaje": "Saldo insuficiente"}), 400
    return jsonify({"mensaje": "Cuenta no encontrada"}), 404

@app.route('/transferir', methods=['POST'])
def transferir():
    id_origen = request.json['id_origen']
    id_destino = request.json['id_destino']
    monto = request.json['monto']
    if banco.transferir(id_origen, id_destino, monto):
        return jsonify({"mensaje": "Transferencia exitosa"}), 200
    return jsonify({"mensaje": "Transferencia fallida"}), 400

if __name__ == '__main__':
    app.run(debug=True)
