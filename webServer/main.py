import time
import random
import json

# from dotenv import load_dotenv
import os

# load_dotenv()

from deta import Deta
from flask import Flask, send_file

deta = Deta(os.getenv("DETA_PROJECT_KEY"))
db = deta.Base(os.getenv("DETA_BASE_NAME"))

app = Flask(__name__)


@app.get("/")
def index():
    """main UI page"""
    return send_file("static/index.html")


@app.get("/reading")
def put_reading():
    """test helper endpoint that puts a random data point into the db"""
    db.put({"value": random.randint(0, 4096)}, str(int(time.time())))
    return "OK"


@app.get("/latest/<timestamp>")
def get_latest(timestamp: float):
    """endpoint to get the latest readings from the data base"""
    # only show readings greater than the provided unix timestamp
    resp = db.fetch(query={"key?gt": timestamp}, limit=1)
    if resp.items:
        return json.dumps(resp.items)
    else:
        return "", 204  # 204 means 'no content in response'


# run server in debug mode if run directly (for local dev)
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=6969)
