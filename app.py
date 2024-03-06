from flask import Flask, render_template, jsonify
import random 
import time
import os

app = Flask(__name__)

# Mock Bluetooth data
def generate_mock_data():
    return {"timestamp": time.time(), "value": random.uniform(0, 10)}

def generate_mock_data2():
    return {"timestamp": time.time(), "value": random.uniform(0,5)}

@app.route('/')
def hello_world():
	return 'Hello World!'

@app.route('/gamma', methods=['GET'])
def index_gamma():
    return render_template('index.html')

@app.route('/beta', methods=['GET'])
def index_beta():
    return render_template('index_beta.html')

@app.route('/get_gamma_data', methods=['GET'])
def get_gamma_data():
    mock_data = generate_mock_data()
    return jsonify(mock_data)

@app.route('/get_beta_data', methods=['GET'])
def get_beta_data():
    mock_data = generate_mock_data2()
    return jsonify(mock_data)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
