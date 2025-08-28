from flask import Flask, jsonify
import json
import random

app = Flask(__name__)

def cargar_datos_json():
    """Carga las curiosidades desde datos.json"""
    try:
        with open('datos.json', 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {"error": "Archivo datos.json no encontrado"}
    except json.JSONDecodeError:
        return {"error": "JSON corrupto"}

@app.route('/trivia/<int:numero>', methods=['GET'])
def obtener_trivia(numero):
    """Endpoint que devuelve la trivia para un número específico"""
    datos = cargar_datos_json()
    numero_str = str(numero)
    
    if numero_str in datos:
        return jsonify({
            "number": numero,
            "text": datos[numero_str],
            "type": "trivia",
            "source": "api_local"
        })
    else:
        return jsonify({
            "error": f"No hay trivia para el número {numero}",
            "number": numero
        }), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='localhost')