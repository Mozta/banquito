
import os
from load_dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_cors import CORS
from banco import Banco
from werkzeug.exceptions import BadRequest

load_dotenv()
app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
banco = Banco()

# Configuracion JWT
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')
jwt = JWTManager(app)


def validar_monto(monto):
    try:
        monto = float(monto)
        if monto <= 0:
            raise ValueError("El monto debe ser positivo")
        return monto
    except ValueError as e:
        raise BadRequest(str(e))


def validar_usuario(username, password):
    print(f"CREDENCIALES: {username} - {password}")
    # TODO: Implementa la logica de validacion auth -> BD
    return True


@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if validar_usuario(username, password):
        access_token = create_access_token(identity=username)
        return jsonify({'token': access_token}), 200
    return jsonify({"mensaje": "Credencias incorrectas"}), 401


@app.route('/crear_cuenta', methods=['POST'])
def crear_cuenta():
    try:
        if banco.crear_cuenta():
            return jsonify({"mensaje": "Cuenta creada exitosamente"}), 201
        else:
            return jsonify({"mensaje": "Hubo un error al crear la cuenta"}), 400
    except Exception as e:
        return jsonify({"mensaje": str(e)}), 500


@app.route('/cuentas/', methods=['GET'])
@jwt_required()
def obtener_cuentas():
    try:
        return jsonify(banco.serializar_cuentas()), 200
    except Exception as e:
        return jsonify({"mensaje": str(e)}), 500


@app.route('/', methods=['GET'])
def home():
    return jsonify({"mensaje": "Bienvenido al banco"}), 200


@app.route('/depositar/<int:id_cuenta>', methods=['POST'])
def depositar(id_cuenta):
    try:
        monto = validar_monto(request.json.get('monto', 0))
        cuenta = banco.obtener_cuenta(id_cuenta)
        if cuenta:
            cuenta.depositar(monto)
            return jsonify({"saldo": cuenta.saldo}), 200
        return jsonify({"mensaje": "Cuenta no encontrada"}), 404
    except BadRequest as e:
        return jsonify({"mensaje": str(e)}), 400
    except Exception as e:
        return jsonify({"mensaje": "Error al procesar la solicitud"}), 500


@app.route('/retirar/<int:id_cuenta>', methods=['POST'])
def retirar(id_cuenta):
    try:
        monto = validar_monto(request.json.get('monto', 0))
        cuenta = banco.obtener_cuenta(id_cuenta)
        if cuenta:
            if cuenta.retirar(monto):
                return jsonify({"saldo": cuenta.saldo}), 200
            return jsonify({"mensaje": "Saldo insuficiente"}), 400
        return jsonify({"mensaje": "Cuenta no encontrada"}), 404
    except BadRequest as e:
        return jsonify({"mensaje": str(e)}), 400
    except Exception as e:
        return jsonify({"mensaje": "Error al procesar la solicitud"}), 500


@app.route('/transferir', methods=['POST'])
def transferir():
    try:
        id_origen = int(request.json.get('id_origen'))
        id_destino = int(request.json.get('id_destino'))
        monto = validar_monto(request.json.get('monto', 0))
        if banco.transferir(id_origen, id_destino, monto):
            return jsonify({"mensaje": "Transferencia exitosa"}), 200
        return jsonify({"mensaje": "Transferencia fallida"}), 400
    except BadRequest as e:
        return jsonify({"mensaje": str(e)}), 400
    except Exception as e:
        return jsonify({"mensaje": "Error al procesar la solicitud"}), 500


if __name__ == '__main__':
    app.run(debug=True)
