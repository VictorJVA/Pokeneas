from flask import Flask
import os
from pokeneas_data import pokeneas
from routes import get_routes

app = Flask(__name__)

# Obtener el ID del contenedor
container_id = os.uname()[1]

# Obtener la ruta para la aplicación
get_routes(app, pokeneas, container_id)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
