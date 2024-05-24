#!/usr/bin/python3
""" app """
from flask import Flask
from models import storage
from api.v1.views import app_views
from os import getenv

app = Flask(__name__)
app.register_blueprint(app_views)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown(self):
    """ the Api status"""
    storage.close()

@web_app.errorhandler(404)
def error_pages_404(error):
    """ errors that returns a JSON-formatted status code"""
    return jsonify((error='Not found'), 404)

if __name__ == "__main__":
    host = getenv('HBNB_API_HOST')
    port = getenv('HBNB_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'
    app.run(host=host, port=port, threaded=True)
