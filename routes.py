from flask import jsonify, render_template_string
import random

def get_routes(app, pokeneas, container_id):
    @app.route('/')
    def home():
        html_template = """
        <html>
        <head><title>Busca Pokenea</title></head>
        <body>
            <h1>Busca Pokenea</h1>
            <p>Para obtener información de un Pokenea en JSON, visita <a href="/pokenea_info">/pokenea_info</a></p>
            <p>Para obtener la imagen y la frase filosófica de un Pokenea, visita <a href="/pokenea_image">/pokenea_image</a></p>
        </html>
        """
        return html_template        

    # Ruta para mostrar información del Pokenea en JSON
    @app.route('/pokenea_info', methods=['GET'])
    def get_pokenea_info():
        pokenea = random.choice(pokeneas)
        response = {
            "id": pokenea["id"],
            "nombre": pokenea["nombre"],
            "altura": pokenea["altura"],
            "habilidad": pokenea["habilidad"],
            "container_id": container_id
        }
        return jsonify(response)

    # Ruta para mostrar la imagen y la frase filosófica de un Pokenea
    @app.route('/pokenea_image', methods=['GET'])
    def get_pokenea_imagen():
        pokenea = random.choice(pokeneas)
        html_template = """
        <html>
        <head><title>Pokenea imagen</title></head>
        <body>
            <h1>{{ nombre }}</h1>
            <img src="{{ imagen }}" alt="Imagen de {{ nombre }}">
            <p><i>{{ frase }}</i></p>
            <p><strong>Contenedor ID:</strong> {{ container_id }}</p>
        </body>
        </html>
        """
        return render_template_string(html_template, 
                                      nombre=pokenea["nombre"], 
                                      imagen=pokenea["imagen"], 
                                      frase=pokenea["frase"], 
                                      container_id=container_id)
