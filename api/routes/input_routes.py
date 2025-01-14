import os
from flask import Blueprint, request, jsonify
from controllers.audioProcessing import butter_lowpass_filter

input_routes = Blueprint('input_routes', __name__)

@input_routes.route('/input', methods=['POST'])
def input_clap():
    """
    Processes the incoming POST request with an audio file, applies a Butterworth low-pass filter
    and returns the filtered data.

    The request should send a file under the 'audio' field in a multipart/form-data format.
    """
    # Check if an audio file is part of the request
    if 'audio' not in request.files:
        return jsonify({"error": "No audio file provided"}), 400
    
    audio_file = request.files['audio']

      # Define the path where the file will be saved
    directory = 'tmp'  # directory to save the file
    if not os.path.exists(directory):
        os.makedirs(directory)  # create the directory if it doesn't exist
    
    # Save the audio file temporarily
    file_path = os.path.join(directory, 'audio_chunk.webm')
    audio_file.save(file_path)

    return jsonify({"message": "Audio processed successfully"})

