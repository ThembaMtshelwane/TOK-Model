import sys
import os

# Add the root directory of the project to the module search path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from flask import Flask
from flask_cors import CORS
from api.routes.system_routes import system_routes

app = Flask(__name__)
CORS(app)

app.register_blueprint(system_routes, url_prefix='/systems')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
