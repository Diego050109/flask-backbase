from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def home():
    return "Servidor Flask funcionando correctamente ✅"

@app.route('/submit', methods=['POST'])
def submit_form():
    data = request.json
    nombre = data.get('nombre')
    email = data.get('email')
    return jsonify({"mensaje": f"Hola {nombre}, tu email es {email}"})

if __name__ == '__main__':
    from os import environ
    app.run(host='0.0.0.0', port=int(environ.get('PORT', 5000)))
