import os
import json
import time

from flask import Flask, request, jsonify, make_response, g
from predict import get_prediction, transform_image, render_prediction

app = Flask('flask-demo-ml')

@app.before_request
def before_request_func():
    g.timings = {}

from functools import wraps
def time_this(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        r = func(*args, **kwargs)
        end = time.time()
        g.timings = (end - start)*1000
        return r
    return wrapper

@app.after_request
def after_request_func(response):
    # just append timings to the output response:
    d = json.loads(response.get_data())
    d['time'] = str(g.timings)
    response.set_data(json.dumps(d))
    return response

@app.route('/', methods=['GET'])
def status():
    return make_response(jsonify('OK'), 200)

@app.route('/predict', methods=['POST'])
@time_this
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