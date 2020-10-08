# import the necessary packages
from threading import Thread
import requests
import time
# initialize the Keras REST API endpoint URL along with the input
# image path
KERAS_REST_API_URL = " http://0.0.0.0:5000/predict"
IMAGE_PATH = "kitten.jpg"
# initialize the number of requests for the stress test along with
# the sleep amount between requests
NUM_REQUESTS = 500
SLEEP_COUNT = 0.05
def call_predict_endpoint(n):
	# load the input image and construct the payload for the request
	image = open(IMAGE_PATH, "rb").read()
	payload = {"file": image}
	# submit the request
	try:		
		r = requests.post(KERAS_REST_API_URL, files=payload).json()
		# ensure the request was sucessful
		if r["class_name"]:
			print("[INFO] thread {} OK Time: {}".format(n, r["time"]))
		# otherwise, the request failed
		else:
			print("[INFO] thread {} FAILED".format(n))
	except:
  		print("[INFO] thread {} FAILED".format(n))
	
# loop over the number of threads
for i in range(0, NUM_REQUESTS):
	# start a new thread to call the API
	t = Thread(target=call_predict_endpoint, args=(i,))
	t.daemon = True
	t.start()
	time.sleep(SLEEP_COUNT)
# insert a long sleep so we can wait until the server is finished
# processing the images
time.sleep(300)