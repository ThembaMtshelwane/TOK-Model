from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(message="Welcome to your Python server!")

@app.route('/about')
def about():
    return jsonify(info="This is a simple Flask server.")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
