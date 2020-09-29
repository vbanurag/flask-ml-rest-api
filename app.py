import os

from flask import Flask, request, jsonify, make_response
from predict import get_prediction, transform_image, render_prediction

app = Flask('flask-demo-ml')

@app.route('/', methods=['GET'])
def status():
    return make_response(jsonify('OK'), 200)

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        file = request.files['file']
        if file is not None:
            input_tensor = transform_image(file)
            prediction_idx = get_prediction(input_tensor)
            class_id, class_name = render_prediction(prediction_idx)
            return jsonify({'class_id': class_id, 'class_name': class_name})



if __name__ == "__main__":
    host = os.environ.get('APP_HOST', '0.0.0.0')
    port = os.environ.get('APP_PORT', 5000)
    app.run(host=host, port=port)