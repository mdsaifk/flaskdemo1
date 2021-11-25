
from flask import Flask

from wsgiref import simple_server

from flask import Flask, session, request, Response, jsonify
import os

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

import atexit
import uuid
import os
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return "Flask app is running"



    
if __name__ == "__main__":
    port = int(os.getenv("PORT"))
    #clApp = ClientApp()
    host = '0.0.0.0'
    httpd = simple_server.make_server(host=host,port=port, app=app)
    httpd.serve_forever()