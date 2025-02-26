#!/usr/bin/python3
"""This is the app file for the api"""

from flask import Flask
from api.v1.views import app_views
from models import storage
from os import getenv

app = Flask(__name__)

app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(exception):
    storage.close()


@app.errorhandler(404)
def not_found(exception):
    """handle 404 erros."""
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    app.run(
        host=getenv('HBNB_API_HOST', '0.0.0.0'),
        port=int(getenv('HBNB_API_PORT', 5000)),
        threaded=True,
        )
