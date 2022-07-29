from dotenv import load_dotenv
import os

load_dotenv()

from deta import Deta
from flask import Flask, send_file

deta = Deta(os.getenv('DETA_PROJECT_KEY'))
db = deta.Base('potmeter')

app = Flask(__name__)


@app.get('/')
def index():
  '''main UI page'''
  return send_file('static/index.html')

@app.get('/latest')
def get_latest():
  '''endpoint to get the latest readings from the data base'''
  # TODO take a "timestamp" parameter and only show readings greater than that
  resp = db.fetch(limit=1)
  if resp.items:
    return resp.items[0]
  else:
    return {}

# run server in debug mode if run directly (for local dev)
if __name__=='__main__':
  app.run(debug=True, host='0.0.0.0', port=6969)