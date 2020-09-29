# PyTorch Flask API

This repo contains a sample code to show how to create a Flask API server by deploying our PyTorch model. This is a sample code which goes with [tutorial](https://pytorch.org/tutorials/intermediate/flask_rest_api_tutorial.html).



## How to 

Install the dependencies:

    pip install -r requirements.txt


Run the Flask server:

    python app.py


From another tab, send the image file in a request:

    curl -X POST -F file=@kitten.jpeg http://localhost:5000/predict

Run Through Docker:

## Build

    docker image build -t flask-ml .

## Run 

    docker run -p 5000:5000 -d flask-ml


## License

The mighty MIT license. Please check `LICENSE` for more details.
