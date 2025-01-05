from flask import Blueprint, request, jsonify
from api.controllers.system import best_impulse_response,convolution

system_routes = Blueprint('system_routes', __name__)

@system_routes.route('/best_impulse_response', methods=['GET'])
def get_best_impulse_response():
    response = best_impulse_response()
    return jsonify({"impulse_response": response})

# Route to compute convolution
@system_routes.route('/convolution', methods=['POST'])
def compute_convolution():
    data = request.get_json()
    input_array = data.get('input_array', [])
    impulse_response = data.get('impulse_response', [])
    
    if not input_array or not impulse_response:
        return jsonify({'error': 'Both input_array and impulse_response are required'}), 400

    # Compute convolution
    result = convolution(input_array, impulse_response)
    return jsonify({'result': result})