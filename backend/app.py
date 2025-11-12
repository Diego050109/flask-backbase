from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os

# Crear la app Flask
app = Flask(__name__, static_folder='../frontend', static_url_path='')
CORS(app)  # Permitir peticiones desde el frontend

# 🏠 Ruta principal: muestra el formulario (index.html)
@app.route('/')
def servir_index():
    return send_from_directory('../frontend', 'index.html')

# 📩 Ruta para manejar el envío del formulario
@app.route('/enviar', methods=['POST'])
def enviar():
    data = request.get_json()
    nombre = data.get('nombre')
    email = data.get('email')
    return jsonify({"mensaje": f"Hola {nombre}, tu email es {email}"})

# 🚀 Ejecutar el servidor
if __name__ == '__main__':
    print("🚀 Iniciando servidor Flask...")
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)
