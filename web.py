from flask import Flask, request, jsonify

app = Flask(__name__)

# Ruta de prueba principal
@app.route('/', methods=['GET'])
def inicio():
    return jsonify({
        "estado": "activo",
        "mensaje": "Servidor del Bot de TikTok funcionando correctamente"
    })

# Ruta para recibir peticiones de resumen
@app.route('/resumir', methods=['POST'])
def resumir():
    # Recibir los datos enviados por la app/burbuja flotante
    datos = request.get_json(silent=True) or {}
    url_tiktok = datos.get('url', '')
    
    if not url_tiktok:
        return jsonify({
            "estado": "error",
            "mensaje": "No se proporcionó ningún enlace de TikTok."
        }), 400

    # Lógica temporal de prueba (Simulación de resumen)
    resumen_generado = f"Este es el resumen procesado para el video: {url_tiktok}"

    return jsonify({
        "estado": "exito",
        "url": url_tiktok,
        "resumen": resumen_generado
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

