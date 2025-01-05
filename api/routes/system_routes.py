from flask import Blueprint, jsonify
from api.controllers.system import best_impulse_response

system_routes = Blueprint('system_routes', __name__)

@system_routes.route('/best_impulse_response', methods=['GET'])
def get_best_impulse_response():
    response = best_impulse_response()
    return jsonify({"impulse_response": response})
