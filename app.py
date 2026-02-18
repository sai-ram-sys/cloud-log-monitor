from flask import Flask
import logging
import random

app = Flask(__name__)

logging.basicConfig(filename='app.log', level=logging.INFO)

@app.route('/')
def home():
    if random.randint(1,5) == 3:
        logging.error("ERROR: Something went wrong!")
        return "Error occurred and logged!"
    else:
        logging.info("INFO: Normal request")
        return "App is running normally."

if __name__ == '__main__':
    app.run()