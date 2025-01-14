import sys
import os

# Add the root directory of the project to the module search path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from flask import Flask
from flask_cors import CORS
from routes.system_routes import system_routes
from routes.input_routes import input_routes

app = Flask(__name__)
CORS(app)

app.register_blueprint(system_routes, url_prefix='/systems')
app.register_blueprint(input_routes, url_prefix='/audio')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
